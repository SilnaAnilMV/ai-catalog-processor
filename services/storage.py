import os
from PIL import Image

class LocalStorageService:

    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_image(self, image: Image.Image, filename: str):
        path    = os.path.join(self.output_dir, filename)
        image.save(path)
        return path