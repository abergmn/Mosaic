"""
logging.py

Custom logging functions for network Mosaic.
"""

from datetime import datetime

def log_error(message: str) -> None:
    """
    Log an error message.

    Args:
        message (str): The error message to log.

    Returns:
        None
    """

    t_time_fmt = datetime.now().strftime("[%Y:%m:%d + %H:%S]")
    print(f"{t_time_fmt} [ERROR]: {message}")

    return

def log_info(message: str) -> None:
    """
    Log an informational message.

    Args:
        message (str): The message to log.

    Returns:
        None
    """

    t_time_fmt = datetime.now().strftime("[%Y:%m:%d + %H:%S]")
    print(f"{t_time_fmt} [INFO]: {message}")

    return
