# src/exception.py
import sys
import traceback
from src.logger import logger

class CustomException(Exception):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(message)
        self.message = message
        self.error = error
        self.log_exception()

    def log_exception(self):
        """
        Logs exception details including stack trace.
        """
        exc_type, exc_value, exc_tb = sys.exc_info()
        stack_trace = traceback.format_exception(exc_type, exc_value, exc_tb)
        logger.error(f"Exception: {self.message}")
        logger.error("".join(stack_trace))

    def __str__(self):
        return f"CustomException: {self.message}"
