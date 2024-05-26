import requests
import datetime
import shutil
import uuid
import os
import re

import os
import shutil

def clear_and_create_directory(directory_path: str) -> bool:
    """Clears and creates a directory, ignoring .log files.

    Args:
    - directory_path (str): Path of the directory to be created.

    Returns:
    - bool: True if directory creation is successful, False otherwise.
    """
    # Check if the directory already exists
    if os.path.exists(directory_path):
        # Iterate over all the files and directories in the given directory
        for item in os.listdir(directory_path):
            item_path = os.path.join(directory_path, item)
            # Check if the item is a .log file
            if os.path.isfile(item_path) and item.endswith('.log'):
                continue
            # Remove the directory or file
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
    else:
        # Create the directory
        os.makedirs(directory_path)

    return True



def download_image(url: str, output_path: str) -> str:
    """Downloads an image from a URL to the specified output path.

    Args:
    - url (str): URL of the image to be downloaded.
    - output_path (str): Path where the downloaded image will be saved.

    Returns:
    - str: Path of the downloaded image.
    """
    image_name = str(uuid.uuid4())
    with open(f"{output_path}/{image_name}.jpg", "wb") as handler:
        handler.write(requests.get(url).content)
    
    return f"{output_path}/{image_name}.jpg"

def get_month_range(number_of_months: int) -> datetime.datetime:
    """Get the start date of a range of months before the current date.

    Args:
    - number_of_months (int): Number of months.

    Returns:
    - datetime.datetime: Start date of the range.
    """
    today = datetime.datetime.now()
    if number_of_months < 2:
        end_date = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    else:
        end_date = today - timedelta(days=30 * (number_of_months - 1))
        end_date = end_date.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return end_date

def contains_money(title: str, description: str) -> bool:
    """Check if either the title or description contains a monetary value.

    Args:
    - title (str): Title string.
    - description (str): Description string.

    Returns:
    - bool: True if either the title or description contains a monetary value, False otherwise.
    """
    money_pattern = re.compile(r"""
        (\$\d{1,3}(,\d{3})*(\.\d{2})?)|  # $11.1 or $111,111.11
        (\d+(\.\d{1,2})?\s*dollars?)|    # dollars
        (\d+(\.\d{1,2})?\s*USD)          # USD
        """, re.VERBOSE | re.IGNORECASE)
    
    return bool(money_pattern.search(title)) or bool(money_pattern.search(description))

def count_phrases(search_phrase: str, title: str, description: str) -> int:
    """Count the occurrences of a search phrase in the title and description.

    Args:
    - search_phrase (str): Search phrase.
    - title (str): Title string.
    - description (str): Description string.

    Returns:
    - int: Total count of occurrences of the search phrase in the title and description.
    """
    title_count = title.lower().count(search_phrase.lower())
    description_count = description.lower().count(search_phrase.lower())
    return title_count + description_count