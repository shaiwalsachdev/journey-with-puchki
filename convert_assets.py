import os
import subprocess

def convert_heic_to_jpg(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.heic'):
                heic_path = os.path.join(dirpath, filename)
                jpg_filename = os.path.splitext(filename)[0] + '.jpg'
                jpg_path = os.path.join(dirpath, jpg_filename)
                
                print(f"Converting {heic_path} to {jpg_path}...")
                try:
                    subprocess.run(["sips", "-s", "format", "jpeg", heic_path, "--out", jpg_path], check=True)
                    # verify creation
                    if os.path.exists(jpg_path):
                         os.remove(heic_path) # Delete original only if success
                         print(f"Success: {jpg_path}")
                    else:
                         print(f"Error: Failed to create {jpg_path}")
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {heic_path}: {e}")

if __name__ == "__main__":
    convert_heic_to_jpg("fastapi_app/static")
