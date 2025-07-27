from PIL import Image, ImageDraw
import os

def crop_transparent_area(image_path, output_path=None, add_gradient=False):
    image = Image.open(image_path).convert("RGBA")
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()

    if not bbox:
        print("Image is fully transparent.")
        return

    cropped = image.crop(bbox)
    alpha_cropped = alpha.crop(bbox)
    width, height = cropped.size

    if add_gradient:
        # Create vertical blue gradient
        gradient = Image.new("RGBA", (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(gradient)

        for y in range(height):
            blue = int(150 + 100 * (y / height))  # from 150 to 250
            draw.line([(0, y), (width, y)], fill=(0, 0, blue, 255))

        # Apply gradient only where image is visible
        gradient_masked = Image.composite(gradient, Image.new("RGBA", (width, height), (0, 0, 0, 0)), alpha_cropped)
        # Combine original image with gradient
        cropped = Image.alpha_composite(cropped, gradient_masked)

    if not output_path:
        name, ext = os.path.splitext(image_path)
        output_path = f"{name}_cropped_gradient{ext if add_gradient else ext}"

    cropped.save(output_path)
    print(f"Saved to: {output_path}")


if __name__ == "__main__":
    img_pth = input("Image path: ")
    crop_transparent_area(img_pth, add_gradient=True)
