# utils/logger.py

import logging
import os

LOG_DIR = "logs"
LOG_FILE = "evaluation.log"

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("evaluation_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Remove any existing handlers to avoid duplication
if logger.hasHandlers():
    logger.handlers.clear()

# File-only logging
file_handler = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE))
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
