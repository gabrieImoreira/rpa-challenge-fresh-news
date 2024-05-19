# RPA Challenge 2.0 - Fresh News

The challenge consist in automate the process of extracting data from a news site >>> https://www.latimes.com/.
The output will be a folder in a ./ouput/results contains a excel results.

## Prerequisites

Ensure you have the following packages installed in your environment:
- [rpaframework](https://rpaframework.org/)
- [pandas](https://pandas.pydata.org/)
- [loguru](https://loguru.readthedocs.io/)

## Installation

You can install the required packages using your preferred virtual environment manager:

### Option 1: Virtual Environment

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate
```

# Install required packages
After you install you can run calling file ```tasks.py``` at the root of the project. 

### Option 2: Pipenv
Using pipenv in a root of the project:

```
pipenv install
```
After you install you can run calling file ```pipenv run robot``` at the root of the project. 

## Output

The extracted data will be stored in the ./output/results folder as an Excel file.

## Notes

Ensure that you have a stable internet connection before running the automation to ensure proper data extraction from the LA Times website.
Feel free to explore and customize the automation process according to your requirements!