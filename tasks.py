from src.crawler_latimes import  LATimesCrawler
import json

if __name__ == '__main__':

    with open("setup.json", "r") as file:
        setup = json.load(file)
        search_phrase = setup["search_phrase"]
        category = setup["topic"]
        number_of_months = setup["number_of_months"]

    with LATimesCrawler() as crawler:  
        crawler.main(search_phrase, category, number_of_months)
        # its possible to run more phrases with the same object, just call the main function again
