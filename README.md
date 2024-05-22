# RPA Challenge 2.0 - Fresh News

The challenge is to automate the data extraction process from a news website >>> https://www.latimes.com/.
The output will be a folder in ./ouput/results that contains excel results and news images.

## Notes
 - This code follows good programming practices by using Object-Oriented Programming (OOP) and following PEP8 guidelines for code style.. It includes logging through decorators to track activities, and each function is thoroughly documented.
 - The code also has retry attempts if the browser breaks, something is not found, in addition, you can place more than one item in the queue using the same object, the code knows how to deal with this.
 - Ensure that you have a stable internet connection before running the automation to ensure proper data extraction from the LA Times website.
- Feel free to explore and customize the automation process according to your requirements!

## Prerequisites

Ensure you have the following packages installed in your environment:
- [rpaframework](https://rpaframework.org/)
- [pandas](https://pandas.pydata.org/)
- [loguru](https://loguru.readthedocs.io/)

## Installation

You need to have pipenv in your environment.
Using pipenv in a root of the project:

```
pipenv install
```
After you install you can run calling file ```pipenv run robot``` at the root of the project. 

## Output

The extracted data will be stored in the ./output/results folder as an Excel file.
