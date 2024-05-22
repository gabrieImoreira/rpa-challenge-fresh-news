from src.crawler_latimes import  LATimesCrawler
import json
from RPA.Robocorp.WorkItems import WorkItems

if __name__ == '__main__':

    wi = WorkItems()
    wi.get_input_work_item()
    search_phrase = wi.get_work_item_variable("search_phrase")
    category = wi.get_work_item_variable("topic")
    number_of_months = wi.get_work_item_variable("number_of_months")

    with LATimesCrawler() as crawler:  
        crawler.main(search_phrase, category, number_of_months)
        # its possible to run more phrases with the same object, just call the main function again