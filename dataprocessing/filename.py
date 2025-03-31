import os

# Set your folder path
folder_path = r"D:\Capstone\Dataset\UE Data2\RGB" 

jpg_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])

# Start indexing from 1341
start_index = 1341

# Rename files sequentially
for index, filename in enumerate(jpg_files, start=start_index):
    new_name = f"rgb_frame_{index:03d}.jpg"  # Example: depth_frame_1341.jpg, depth_frame_1342.jpg
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {new_name}")

print("Renaming completed!")
