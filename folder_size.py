import os

folder_path = input("Enter folder path: ")

total_size = 0

for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.isfile(file_path):
            total_size += os.path.getsize(file_path)

size_mb = total_size / (1024 * 1024)

print(f"\nTotal folder size: {size_mb:.2f} MB")
