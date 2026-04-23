from PIL import Image, ImageEnhance
from rembg import remove
import io


def remove_background(input_path):
    with open(input_path, "rb") as f:
        input_bytes = f.read()

    output_bytes    = remove(input_bytes)
    img             = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

    white_bg        = Image.new("RGBA", img.size, (255, 255, 255, 255))
    final_img       = Image.alpha_composite(white_bg, img)

    return final_img.convert("RGB")


def enhance_image(image: Image.Image):
    image   = ImageEnhance.Sharpness(image).enhance(2.0)
    image   = ImageEnhance.Brightness(image).enhance(1.2)
    return image


def creative_variant(image: Image.Image, prompt: str):
    prompt      = prompt.lower()

    if "dark" in prompt:
        image   = ImageEnhance.Brightness(image).enhance(0.7)

    if "bright" in prompt:
        image   = ImageEnhance.Brightness(image).enhance(1.5)

    if "sharp" in prompt:
        image   = ImageEnhance.Sharpness(image).enhance(2.0)

    return image