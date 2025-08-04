import os
from PIL import Image

def get_png_files():
    return [f for f in os.listdir() if f.lower().endswith('.png') and os.path.isfile(f)]

def get_image_size(file):
    with Image.open(file) as img:
        return img.size  # (width, height)

def get_smallest_png(png_files):
    min_area = float('inf')
    smallest_file = None
    smallest_size = None
    for file in png_files:
        size = get_image_size(file)
        area = size[0] * size[1]
        if area < min_area:
            min_area = area
            smallest_file = file
            smallest_size = size
    return smallest_file, smallest_size

def resize_images_to_fit_target(png_files, target_size, exclude_file):
    target_width, target_height = target_size
    for file in png_files:
        if file == exclude_file:
            continue
        with Image.open(file) as img:
            width, height = img.size

            # Calculate scale factor to preserve aspect ratio
            scale = min(target_width / width, target_height / height)
            new_size = (int(width * scale), int(height * scale))

            resized = img.resize(new_size, Image.LANCZOS)
            resized.save(file)
            print(f"Resized {file} to {new_size}")

def main():
    png_files = get_png_files()
    if not png_files:
        print("No PNG files found in the current directory.")
        return

    smallest_file, smallest_size = get_smallest_png(png_files)
    print(f"Smallest image: {smallest_file} with size {smallest_size}")
    
    resize_images_to_fit_target(png_files, smallest_size, smallest_file)

if __name__ == "__main__":
    main()
