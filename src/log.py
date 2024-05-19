import traceback
from functools import wraps
from sys import stderr
from loguru import logger
from datetime import datetime

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

logger.add(
    f"output/log_{current_time}.log",
    format="{time:YYYY-MM-DD HH:mm:ss} {level} {message} {file}",
    level="INFO"
)

def log_decorator(func):
    """Decorator function to log function calls and exceptions."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper function to log function calls and exceptions."""
        logger.info(f"Started function '{func.__name__}' with args {args} and kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' returns {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception in function '{func.__name__}': {traceback.format_exc()}")
            raise e
    return wrapper