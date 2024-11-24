import sys
import traceback
from logger import get_logger

# Initialize the logger
logger = get_logger()

class CustomException(Exception):
    """
    A custom exception class for handling errors in the ML project.

    Attributes:
        message (str): The error message to be displayed.
        details (str): Detailed traceback of the original exception.
    """

    def __init__(self, message, original_exception=None):
        """
        Initializes the CustomException class.

        Args:
            message (str): A description of the error.
            original_exception (Exception, optional): The original exception instance.
        """
        super().__init__(message)
        self.message = message
        self.details = self.get_error_details(original_exception)
        
        # Log the error
        logger.error(f"Error occurred: {self.message}")
        if self.details != "No additional details provided.":
            logger.error(f"Details: {self.details}")

    @staticmethod
    def get_error_details(original_exception):
        """
        Retrieves detailed traceback information for the original exception.

        Args:
            original_exception (Exception): The original exception instance.

        Returns:
            str: The formatted traceback details as a string.
        """
        if original_exception is None:
            return "No additional details provided."
        exc_type, exc_value, exc_traceback = sys.exc_info()
        return "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))

    def __str__(self):
        """
        Returns the string representation of the exception.
        """
        return f"{self.message}\nDetails: {self.details}"
