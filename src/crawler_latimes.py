from src.provider.browser_provider import GenericBrowser
from src.resources import selectors_latimes as selectors
from src import utils
from dateutil import parser
from datetime import datetime, timedelta
import traceback
import time
import os



class LATimesCrawler:
    def __init__(self):
        self.url = os.getenv('LATIMES_URL')
        self.img_path = os.getenv('IMG_PATH')
        self.browser = GenericBrowser()
    
    def main(self, search_phrase: str, topic: str, number_of_months: int):
        utils.clear_and_create_directory(self.img_path)
        self.search_news(search_phrase, topic)
        result = self.get_news(number_of_months)
        self.mount_output_file()

        # verificar se navegador está aberto, se n tiver abrir
        # pesquisar pela noticia, filtrar o necessário
        # verificar tempo da noticia
        # fazer download da imagem e montar dicionario
        # fazer isso para todas as noticias
        # retornar dicionario
        # montar arquivo de saida

    def search_news(self, search_phrase: str, topic: str):

        self.open_browser_if_not_already_open()
        # Click on search button
        self.browser.wait_until_element_is_visible(selectors.btn_search, timeout=30)
        self.browser.click_element(selectors.btn_search)
        # Search for the phrase
        self.browser.input_text(selectors.input_search, search_phrase)
        self.browser.click_element(selectors.btn_submit_search)
        # Sort by newest
        self.browser.wait_until_element_is_enabled(selectors.select_sort_by, timeout=30)
        self.browser.select_from_list_by_label(selectors.select_sort_by, "Newest")
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=10)
        # Filter by topic
        self.browser.wait_until_element_is_enabled(selectors.input_topic.format(topic=topic), timeout=30)
        self.browser.click_element(selectors.input_topic.format(topic=topic))
        # time.sleep(1)

    def open_browser_if_not_already_open(self):
        try:
            self.browser.get_current_url()
        except:
            self.browser = self.browser.open_default_browser(self.url)

    def get_news(self, number_of_months: int):
        # Wait Js load
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=10)
        time.sleep(2)
        # No results found
        result = self.browser.get_element_count(selectors.menu_no_results)
        if result > 0:
            return []
        start_date = utils.get_month_range(number_of_months)
        print('start data', start_date)
        # Get news
        list_news = []
        results_per_page = self.browser.get_element_count(selectors.menu_search_results)
        for i in range(1, results_per_page + 1):
            date = self.browser.get_text(selectors.menu_search_results_timestamp.format(count=i))
            title = self.browser.get_text(selectors.menu_search_results_title.format(count=i))
            description = self.browser.get_text(selectors.menu_search_results_description.format(count=i))
            img_url = self.browser.get_element_attribute(selectors.menu_search_results_img.format(count=i), "src")
            img_path = utils.download_image(img_url, self.img_path)
            
            date = parser.parse(date, fuzzy=True).strftime('%Y/%m/%d')
            
            list_news.append({
                "title": title,
                "date": date,
                "description": description,
                "img_path": img_path
            })
        
        return list_news

    def mount_output_file(self):
        pass
