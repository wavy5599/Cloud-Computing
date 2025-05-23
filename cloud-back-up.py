import os
import shutil
import time

# === CONFIGURATION ===
source_folder = r"C:\Users\morri\OneDrive\Desktop"
icloud_folder = r"C:\Users\morri\iCloudDrive"  # Make sure this is the correct path
sync_interval = 5  # Check every 5 seconds

# === SYNC FUNCTION ===
def sync_to_icloud():
    for filename in os.listdir(source_folder):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(icloud_folder, filename)

        if os.path.isfile(src_path):
            if not os.path.exists(dst_path):
                shutil.copy2(src_path, dst_path)
                print(f"Synced file: {filename}")
            else:
                print(f"File already exists in iCloud: {filename}")
                
        elif os.path.isdir(src_path):
            if not os.path.exists(dst_path):
                shutil.copytree(src_path, dst_path)
                print(f"Synced folder: {filename}")
            else:
                print(f"Folder already exists in iCloud: {filename}")

# === MAIN LOOP ===
def main():
    print("Syncing to iCloud Drive... Press Ctrl+C to stop.")
    while True:
        sync_to_icloud()
        time.sleep(sync_interval)

if __name__ == "__main__":
    main()
