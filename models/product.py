from dataclasses import dataclass

@dataclass
class Product:
    sku         : str
    name        : str
    category    : str
    image_path  : str