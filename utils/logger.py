import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    os.makedirs("logs", exist_ok=True)

    logger      = logging.getLogger("catalog_processor")
    logger.setLevel(logging.INFO)

    handler     = RotatingFileHandler(
                    "logs/app.log",
                    maxBytes=1_000_000,
                    backupCount=3
                )

    formatter   = logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
                )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

logger          = setup_logger()