# AI Catalog Processing System

## Overview

This project is a mini AI-powered catalog processing system that processes product images and metadata.

---

## Features

* Background removal and image enhancement
* Creative image generation based on prompt
* Parallel image processing
* Versioned output
* Simple Streamlit UI

---

## Tech Stack

* Python
* Streamlit
* PIL
* rembg
* Pandas

---

## Setup Instructions

```bash
pip install -r requirements.txt
set PYTHONPATH=.
streamlit run ui/app.py
```

---

## System Design

The system is designed to scale using a distributed architecture with queue-based processing and worker nodes.

See `architecture.md` for detailed explanation.

---

## Folder Structure

```text
core/       - Processing logic
models/     - Data models
services/   - Storage services
utils/      - Logging and helpers
ui/         - Streamlit UI
```

---


## Sample Data & Demo

A sample dataset is included in the `sample-data/` folder to help you quickly test the system.

###  Contents

* `products.csv` -> Example product metadata file
* `images/` -> Sample product images
* `demo.mp4` -> Short demo video showing the system in action

---

###  How to Use Sample Data

1. Run the application:

```bash
streamlit run ui/app.py
```

2. In the UI:

* Upload: `sample-data/products.csv`
* Set Image Folder: `sample-data/images`
* Enter a prompt (e.g., *dark modern style*)

3. Click **Start Processing**

---

###  Demo

A demo video is available at:

```text
sample-data/demo-video/ai-catelog-processor.mp4
```

This video shows:

* Uploading CSV and images
* Running the processing pipeline
* Viewing output images

---

###  Notes

* The sample data is for demonstration purposes only
* You can replace it with your own dataset
* Ensure your CSV includes a `sku` column



## Future Improvements

* Replace ThreadPool with ProcessPool for CPU tasks
* Add async API integration
* Deploy with Celery + Redis for distributed processing



## Additional sections:
- architecture.md -> system design
- leadership.md -> management & communication