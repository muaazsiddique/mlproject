# src/logger.py
import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime

# Directory where logs will be stored
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Log file path
LOG_FILE = os.path.join(LOG_DIR, f"ml_project_{datetime.now().strftime('%Y-%m-%d')}.log")

def setup_logger(log_file=LOG_FILE):
    """
    Set up the logger for the project with rotating file handler.
    Args:
        log_file (str): Path where the log file will be stored.
    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler
        file_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Get the logger
logger = setup_logger()
