import os
import sys
import shutil

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from media_optimizer import optimize_file_bytes

def compress_folder(src, dst):
    if not os.path.exists(dst):
        os.makedirs(dst)
        
    files = [f for f in os.listdir(src) if f.lower().endswith(('.heic', '.jpg', '.jpeg', '.png', '.mp4', '.mov'))]
    for filename in files:
        filepath = os.path.join(src, filename)
        print(f"Compressing {filename}...")
        with open(filepath, "rb") as f:
            content = f.read()
            
        opt_bytes, new_filename, _ = optimize_file_bytes(content, filename)
        
        dst_path = os.path.join(dst, new_filename)
        with open(dst_path, "wb") as f:
            f.write(opt_bytes)
        print(f"Saved optimized file to {dst_path}")

if __name__ == "__main__":
    src_folder = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001 2"
    dst_folder = "/Users/geekdon/Documents/Journey with Puchki/Photos-3-001 2 Compressed"
    compress_folder(src_folder, dst_folder)
