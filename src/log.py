import traceback
from functools import wraps
import logging
from datetime import datetime

current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
logging.basicConfig(
    filename=f"output/log_{current_time}.log",
    filemode='a',
    format='%(asctime)s %(levelname)s %(message)s %(filename)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s %(filename)s'))

logger.addHandler(stream_handler)

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