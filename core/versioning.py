import os

def get_next_version(output_dir, sku):
    version     = 1

    while True:
        image1  = os.path.join(output_dir, f"{sku}_v{version}_image1.jpg")
        image2  = os.path.join(output_dir, f"{sku}_v{version}_image2.jpg")

        if not os.path.exists(image1) and not os.path.exists(image2):
            return version

        version += 1