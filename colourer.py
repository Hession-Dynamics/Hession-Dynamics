from PIL import Image
import os

def replace_color_with_black(image_path):
    with Image.open(image_path).convert("RGBA") as img:
        pixels = img.load()
        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]
                if a != 0:  # Only replace visible (non-transparent) pixels
                    pixels[x, y] = (0, 0, 0, a)

        img.save(image_path)
        print(f"Converted {image_path} to pitch black (preserving transparency)")

def main():
    for file in os.listdir():
        if file.lower().endswith(".png") and os.path.isfile(file):
            replace_color_with_black(file)

if __name__ == "__main__":
    main()
