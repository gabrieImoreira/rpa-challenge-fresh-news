from src.crawler_latimes import  LATimesCrawler
# from RPA.Robocorp.WorkItems import WorkItems

if __name__ == '__main__':
    # Credentials doesn't work, so I will use the default values
    # wi = WorkItems()
    # wi.get_input_work_item()
    # search_phrase = wi.get_work_item_variable("search_phrase")
    # category = wi.get_work_item_variable("topic")
    # number_of_months = wi.get_work_item_variable("number_of_months")

    with open("setup.json", "r") as file:
        setup = json.load(file)
        search_phrase = setup["search_phrase"]
        category = setup["topic"]
        number_of_months = setup["number_of_months"]

    with LATimesCrawler() as crawler:  
        crawler.main(search_phrase, category, number_of_months)