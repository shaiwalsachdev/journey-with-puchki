"""
One-time migration: Upload all media from static/uploads/ to Cloudflare R2.
Run from project root: python migrate_to_r2.py

Requires environment variables:
  R2_ACCESS_KEY_ID
  R2_SECRET_ACCESS_KEY
"""
import os
import sys

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fastapi_app")
UPLOADS_DIR = os.path.join(BASE_DIR, "static", "uploads")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fastapi_app.storage import upload_file_from_path, R2_PUBLIC_URL

# Supported extensions
MEDIA_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.heic', '.mp4', '.mov', '.mp3'}

def migrate():
    if not os.path.exists(UPLOADS_DIR):
        print(f"❌ Uploads directory not found: {UPLOADS_DIR}")
        return
    
    total_files = 0
    total_bytes = 0
    errors = []
    
    # Walk through all memory folders
    memory_folders = sorted(os.listdir(UPLOADS_DIR))
    
    for folder_name in memory_folders:
        folder_path = os.path.join(UPLOADS_DIR, folder_name)
        if not os.path.isdir(folder_path):
            continue
        
        files = os.listdir(folder_path)
        media_files = [f for f in files if os.path.splitext(f)[1].lower() in MEDIA_EXTENSIONS]
        
        if not media_files:
            print(f"📁 {folder_name}/ — No media files, skipping")
            continue
        
        print(f"\n📁 {folder_name}/ — {len(media_files)} files")
        
        for filename in sorted(media_files):
            local_path = os.path.join(folder_path, filename)
            r2_key = f"uploads/{folder_name}/{filename}"
            file_size = os.path.getsize(local_path)
            
            try:
                url = upload_file_from_path(local_path, r2_key)
                total_files += 1
                total_bytes += file_size
                size_mb = file_size / (1024 * 1024)
                print(f"   ✅ {filename} ({size_mb:.1f} MB) → {url}")
            except Exception as e:
                errors.append((r2_key, str(e)))
                print(f"   ❌ {filename} — ERROR: {e}")
    
    # Summary
    total_mb = total_bytes / (1024 * 1024)
    print(f"\n{'='*60}")
    print(f"🎉 Migration Complete!")
    print(f"   Files uploaded: {total_files}")
    print(f"   Total size: {total_mb:.1f} MB")
    print(f"   Public URL base: {R2_PUBLIC_URL}")
    
    if errors:
        print(f"\n⚠️  {len(errors)} errors:")
        for key, err in errors:
            print(f"   - {key}: {err}")
    else:
        print(f"   Errors: None ✅")
    
    print(f"\n📌 Your photos are now at:")
    print(f"   {R2_PUBLIC_URL}/uploads/{{memory_id}}/{{filename}}")

if __name__ == "__main__":
    migrate()
