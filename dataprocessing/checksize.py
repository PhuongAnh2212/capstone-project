import os
from PIL import Image

# Set your folder path
folder_path = r"D:\Capstone\Dataset\UE Data\Semantic"  # Use raw string (r"") to avoid path issues

# Get all jpg files
jpg_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')])

# Check size of each frame
for filename in jpg_files:
    file_path = os.path.join(folder_path, filename)
    
    with Image.open(file_path) as img:
        width, height = img.size  # Get dimensions
    
    print(f"{filename}: {width}x{height}")

print("Size check completed!")
