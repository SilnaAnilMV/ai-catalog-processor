import streamlit as st
import os
import pandas as pd
import glob
from PIL import Image

from core.processor import process_catalog
from collections import defaultdict

st.title("AI Catalog Processor")

st.sidebar.header("Inputs")

csv_file        = st.sidebar.file_uploader("Upload CSV", type=["csv"])
image_folder    = st.sidebar.text_input("Image Folder Path")
output_folder   = st.sidebar.text_input("Output Folder", "output")

#  Prompt required
prompt          = st.text_input(
                    "Creative Prompt",
                    placeholder="e.g., dark modern style, bright minimal, luxury look"
                )

# -------------------------------
# Show CSV Preview + Validation
# -------------------------------
valid_csv           = False

if csv_file:
    try:
        df_preview  = pd.read_csv(csv_file)

        # Normalize columns
        df_preview.columns  = df_preview.columns.str.strip().str.lower()

        st.subheader(" Product Data Preview")
        st.dataframe(df_preview.head())

        # Validate required column
        if "sku" not in df_preview.columns:
            st.error(" CSV must contain a 'sku' column")
            st.info(" Example format: sku, name, category")
        else:
            valid_csv   = True
            st.success(" CSV format looks good")

        # Reset pointer
        csv_file.seek(0)

    except Exception as e:
        st.error(f"Error reading CSV: {e}")


# -------------------------------
# Button (only enabled if valid)
# -------------------------------
start   = st.button(
            "Start Processing",
            disabled=not (csv_file and image_folder and prompt.strip() and valid_csv)
        )

# -------------------------------
# Processing
# -------------------------------
if start:

    try:
        os.makedirs("temp", exist_ok=True)
        csv_path    = "temp/input.csv"

        with open(csv_path, "wb") as f:
            f.write(csv_file.read())

        with st.spinner("Processing..."):
            success, total  = process_catalog(
                                csv_path,
                                image_folder,
                                output_folder,
                                prompt
                            )

        st.success(f"Processed {success}/{total} images")

        # -------------------------------
        # Show Output Images (Grouped)
        # -------------------------------
        st.subheader("Sample Output Images")

        image_paths     = sorted(glob.glob(f"{output_folder}/*.jpg"))

        if image_paths:

            grouped     = defaultdict(list)

            # Group by SKU
            for path in image_paths:
                filename= os.path.basename(path)
                sku     = filename.split("_")[0]   # SKU001
                grouped[sku].append(path)

            # Show max 3 SKUs
            for sku, paths in list(grouped.items())[:5]:

                st.markdown(f"###  {sku}")

                cols    = st.columns(2)

                # Sort to ensure image1 comes before image2
                for i, img_path in enumerate(sorted(paths)):
                    img     = Image.open(img_path)

                    label   = "Clean Image" if "image1" in img_path else "Creative Variant"

                    cols[i % 2].image(
                        img,
                        caption = f"{label} ({os.path.basename(img_path)})",
                        width   = "stretch"
                    )

        else:
            st.warning("No output images found.")

    except ValueError as e:
        st.error(f" {str(e)}")

    except Exception as e:
        st.error(" Unexpected error occurred")
        st.exception(e)