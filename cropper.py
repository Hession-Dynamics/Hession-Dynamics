from PIL import Image
import os

def crop_transparent_area(image_path, output_path=None):
    # Open image
    image = Image.open(image_path).convert("RGBA")
    # Get alpha channel
    alpha = image.getchannel("A")
    # Get bounding box of non-transparent areas
    bbox = alpha.getbbox()

    if bbox:
        # Crop image to non-transparent bounding box
        cropped = image.crop(bbox)
        if not output_path:
            name, ext = os.path.splitext(image_path)
            output_path = f"{name}_cropped{ext}"
        cropped.save(output_path)
        print(f"Cropped image saved to: {output_path}")
    else:
        print("Image is fully transparent, nothing to crop.")

# Example usage
if __name__ == "__main__":
    img_pth = input("Image path: ")
    crop_transparent_area(img_pth)