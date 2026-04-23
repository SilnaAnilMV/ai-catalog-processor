import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from models.product import Product
from core.image_service import remove_background, enhance_image, creative_variant
from core.versioning import get_next_version
from services.storage import LocalStorageService
from utils.logger import logger


def find_image_by_sku(image_folder, sku):
    for ext in [".jpg", ".jpeg", ".png"]:
        path    = os.path.join(image_folder, f"{sku}{ext}")
        if os.path.exists(path):
            return path
    return None


def process_single(product: Product, storage: LocalStorageService, prompt: str):
    try:
        # Retry mechanism
        for attempt in range(3):
            try:
                clean_img   = remove_background(product.image_path)
                break
            except Exception as e:
                if attempt == 2:
                    raise e

        clean_img           = enhance_image(clean_img)

        version             = get_next_version(storage.output_dir, product.sku)

        clean_filename      = f"{product.sku}_v{version}_image1.jpg"
        creative_filename   = f"{product.sku}_v{version}_image2.jpg"

        storage.save_image(clean_img, clean_filename)

        creative_img        = creative_variant(clean_img, prompt)
        storage.save_image(creative_img, creative_filename)

        logger.info(f"Processed {product.sku}")
        return True

    except Exception as e:
        logger.error(f"Error processing {product.sku}: {e}")
        return False


def process_catalog(csv_path, image_folder, output_dir, prompt):
    df          = pd.read_csv(csv_path)
    df.columns  = df.columns.str.strip().str.lower()

    if "sku" not in df.columns:
        raise ValueError("CSV must contain 'sku' column")

    products    = []

    for _, row in df.iterrows():
        sku         = str(row["sku"]).strip()
        image_path  = find_image_by_sku(image_folder, sku)

        if not image_path:
            logger.warning(f"No image for SKU: {sku}")
            continue

        products.append(Product(
            sku         = sku,
            name        = row.get("name", ""),
            category    = row.get("category", ""),
            image_path  = image_path
        ))

    storage     = LocalStorageService(output_dir)

    worker      = partial(process_single, storage=storage, prompt=prompt)

    max_workers = min(32, (os.cpu_count() or 1) * 2)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(worker, products))

    success     = sum(results)

    return success, len(products)