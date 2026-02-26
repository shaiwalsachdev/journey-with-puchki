"""
Cloudflare R2 Storage Helper
S3-compatible object storage for media files.
"""
import os
import boto3
from botocore.config import Config

R2_ACCESS_KEY_ID = os.getenv("R2_ACCESS_KEY_ID", "9c504875759601c84b9217bf03d36b48")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY", "2ea6bae4376041d086cbda6ce805705ac1d176fcc0d9b3056c321d066f19cd1a")
R2_ENDPOINT = os.getenv("R2_ENDPOINT", "https://9b34f848b94e18d6b7bc33fb55424119.r2.cloudflarestorage.com")
R2_BUCKET_NAME = os.getenv("R2_BUCKET_NAME", "puchki-media")
R2_PUBLIC_URL = os.getenv("R2_PUBLIC_URL", "https://pub-5febf239be824301b333f51d2eaee417.r2.dev")

_s3_client = None

def get_s3_client():
    global _s3_client
    if _s3_client is None:
        _s3_client = boto3.client(
            "s3",
            endpoint_url=R2_ENDPOINT,
            aws_access_key_id=R2_ACCESS_KEY_ID,
            aws_secret_access_key=R2_SECRET_ACCESS_KEY,
            config=Config(signature_version="s3v4"),
            region_name="auto",
        )
    return _s3_client


def upload_file(file_obj, key: str, content_type: str = None):
    """
    Upload a file-like object to R2.
    key: e.g. "uploads/21/IMG_9817.jpg"
    Returns the public URL.
    """
    s3 = get_s3_client()
    extra_args = {}
    if content_type:
        extra_args["ContentType"] = content_type
    
    s3.upload_fileobj(file_obj, R2_BUCKET_NAME, key, ExtraArgs=extra_args)
    return get_public_url(key)


def upload_file_from_path(local_path: str, key: str):
    """
    Upload a local file to R2.
    local_path: full path to the file on disk
    key: e.g. "uploads/21/IMG_9817.jpg"
    Returns the public URL.
    """
    s3 = get_s3_client()
    
    # Guess content type
    import mimetypes
    content_type, _ = mimetypes.guess_type(local_path)
    extra_args = {}
    if content_type:
        extra_args["ContentType"] = content_type
    
    s3.upload_file(local_path, R2_BUCKET_NAME, key, ExtraArgs=extra_args)
    return get_public_url(key)


def delete_file(key: str):
    """Delete a file from R2."""
    s3 = get_s3_client()
    s3.delete_object(Bucket=R2_BUCKET_NAME, Key=key)


def get_public_url(key: str) -> str:
    """
    Get the public URL of a file in R2.
    e.g. "uploads/21/IMG_9817.jpg" -> "https://pub-xxx.r2.dev/uploads/21/IMG_9817.jpg"
    """
    return f"{R2_PUBLIC_URL}/{key}"


def get_photo_url(memory_id: int, filename: str) -> str:
    """
    Convenience function: get the public URL for a memory photo.
    """
    return get_public_url(f"uploads/{memory_id}/{filename}")
