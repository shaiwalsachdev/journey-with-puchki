"""
media_optimizer.py — Web-quality media compression shared module.
Photos: → WebP 85%, max 1440px (Instagram-level quality, perfect for web)
Videos: → H.264 MP4 1080p CRF 23 (web-optimized, faststart)
"""

import os
import io
import subprocess
import tempfile
from PIL import Image

# Register HEIC support
try:
    from pillow_heif import register_heif_opener
    register_heif_opener()
except ImportError:
    pass

# Settings — Instagram-quality for web
MAX_PX       = 1440
WEBP_QUALITY = 85
VIDEO_CRF    = 23
VIDEO_HEIGHT = 1080

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".heif"}
VIDEO_EXTS = {".mov", ".mp4", ".avi", ".mkv", ".webm"}


def _find_ffmpeg() -> str:
    """Find ffmpeg binary — homebrew or system PATH."""
    for path in ["/opt/homebrew/bin/ffmpeg", "/usr/local/bin/ffmpeg", "ffmpeg"]:
        if path == "ffmpeg" or os.path.isfile(path):
            return path
    raise RuntimeError("ffmpeg not found. Install with: brew install ffmpeg")


def optimize_image_bytes(content: bytes, original_filename: str) -> tuple[bytes, str, str]:
    """
    Convert any image (incl. HEIC) to WebP 85%, resized to max 1440px.
    Returns: (webp_bytes, new_filename, 'image/webp')
    """
    img = Image.open(io.BytesIO(content))
    img = img.convert("RGB")

    # Resize if larger than MAX_PX on either dimension
    w, h = img.size
    if w > MAX_PX or h > MAX_PX:
        ratio = min(MAX_PX / w, MAX_PX / h)
        img = img.resize((int(w * ratio), int(h * ratio)), Image.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, format="WEBP", quality=WEBP_QUALITY, method=6)
    buf.seek(0)

    base = os.path.splitext(original_filename)[0]
    new_filename = base + ".webp"
    return buf.read(), new_filename, "image/webp"


def optimize_video_file(src_path: str) -> tuple[str, str]:
    """
    Re-encode video to H.264 MP4 1080p CRF 23, web-optimised (faststart).
    Returns: (dst_path, new_filename)
    The caller is responsible for cleaning up dst_path.
    """
    ffmpeg = _find_ffmpeg()
    base = os.path.splitext(os.path.basename(src_path))[0]
    new_filename = base + ".mp4"

    # Write to a sibling tmp file
    dst_path = src_path + "_opt.mp4"

    cmd = [
        ffmpeg, "-y", "-i", src_path,
        "-map", "0:v:0", "-map", "0:a:0?",  # first video + optional audio
        "-vf", f"scale=-2:{VIDEO_HEIGHT},format=yuv420p",
        "-c:v", "libx264", "-crf", str(VIDEO_CRF), "-preset", "slow",
        "-profile:v", "high", "-level", "4.1",
        "-movflags", "+faststart",
        "-c:a", "aac", "-b:a", "128k", "-ar", "44100",
        dst_path
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=600)
    if result.returncode != 0:
        raise RuntimeError(
            f"ffmpeg failed for {os.path.basename(src_path)}:\n"
            + result.stderr.decode()[-400:]
        )
    return dst_path, new_filename


def optimize_file_bytes(
    content: bytes, original_filename: str
) -> tuple[bytes, str, str]:
    """
    Dispatch to photo or video optimizer.
    For videos: writes to a temp file, runs ffmpeg, reads back.
    Returns: (optimized_bytes, new_filename, content_type)
    """
    ext = os.path.splitext(original_filename)[1].lower()

    if ext in IMAGE_EXTS:
        return optimize_image_bytes(content, original_filename)

    elif ext in VIDEO_EXTS:
        with tempfile.NamedTemporaryFile(suffix=ext, delete=False) as tmp:
            tmp.write(content)
            tmp_src = tmp.name
        try:
            dst_path, new_filename = optimize_video_file(tmp_src)
            with open(dst_path, "rb") as f:
                opt_bytes = f.read()
            os.unlink(dst_path)
        finally:
            os.unlink(tmp_src)
        return opt_bytes, new_filename, "video/mp4"

    else:
        # Unknown type — return as-is
        return content, original_filename, "application/octet-stream"
