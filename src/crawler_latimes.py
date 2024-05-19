from src.provider.browser_provider import GenericBrowser
from src.resources import selectors_latimes as selectors
from datetime import datetime, timedelta
from src.log import log_decorator
from dateutil import parser
from loguru import logger
from src import utils
import pandas as pd
import traceback
import time
import os
import re

class LATimesCrawler:
    """Class for crawling LATimes website and retrieving news."""
    def __init__(self):
        self.url = 'https://www.latimes.com/'
        self.results_path = 'output/results'
        self.output_path = 'output'
        self.browser = None
        self.retries = 3
    
        utils.clear_and_create_directory(self.results_path)
    
    def __enter__(self):
        """Initialize LATimesCrawler."""
        logger.info("Entering context and initializing LATimesCrawler")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit context and clean up LATimesCrawler.

        Parameters:
        - exc_type (type): The type of the exception.
        - exc_value (Exception): The exception instance.
        - traceback (Traceback): The traceback object.
        """
        logger.info("Exiting context and cleaning up LATimesCrawler")
        try:
            self.browser.close_browser()
            logger.info("Browser closed successfully in __exit__")
        except Exception as e:
            logger.exception(f"Exception in __exit__: {e}")
    
    @log_decorator
    def main(self, search_phrase: str, topic: str, number_of_months: int) -> None:
        """
        Main method for crawling news.

        Parameters:
        - search_phrase (str): The phrase to search for.
        - topic (str): The topic to filter news by.
        - number_of_months (int): Number of months to consider.

        Returns:
        - None
        """
        attempt = 0
        while True:
            try:
                if self.retries == attempt:
                    break
                self.search_news(search_phrase, topic)
                result = self.get_news(search_phrase, number_of_months)
                self.mount_output_file(search_phrase, result)
                break
            except:
                attempt+=1
                logger.exception(f"Exception in main loop: {traceback.format_exc()}, attempt {attempt}")

    @log_decorator
    def search_news(self, search_phrase: str, topic: str) -> None:
        """
        Search for news based on search phrase and topic.

        Parameters:
        - search_phrase (str): The phrase to search for.
        - topic (str): The topic to filter news by.

        Returns:
        - None
        """
        self.open_browser_if_not_already_open()
        # Click on search button
        self.browser.wait_until_element_is_visible(selectors.btn_search, timeout=30)
        self.browser.click_element(selectors.btn_search)
        # Search for the phrase
        self.browser.input_text(selectors.input_search, search_phrase)
        self.browser.click_element(selectors.btn_submit_search)
        # Filter by topic
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=30)
        topic_exist = self.browser.get_element_count(selectors.input_topic.format(topic=topic))
        if topic_exist == 0:
            logger.info(f"Topic {topic} not found")
        else:
            self.browser.wait_until_element_is_enabled(selectors.input_topic.format(topic=topic), timeout=30)
            self.browser.click_element(selectors.input_topic.format(topic=topic))
        # Sort by newest
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=30)
        time.sleep(2)
        self.browser.wait_until_element_is_visible(selectors.select_sort_by, timeout=30)
        self.browser.select_from_list_by_label(selectors.select_sort_by, "Newest")
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=30)

    @log_decorator
    def open_browser_if_not_already_open(self):
        """Open browser if not already open."""
        try:
            self.browser.go_to(self.url)
        except:
            self.browser = GenericBrowser(headless=False)
            self.browser = self.browser.open_default_browser(self.url)

    @log_decorator
    def get_news(self, search_phrase: str, number_of_months: int) -> list:
        """
        Get news based on search phrase and number of months.

        Parameters:
        - search_phrase (str): The phrase to search for.
        - number_of_months (int): Number of months to consider.

        Returns:
        - list: List of news items.
        """
        # Wait Js load
        self.browser.wait_for_condition('return document.readyState == "complete"', timeout=30)
        # No results found, forced delay for page loading
        try:self.browser.wait_until_element_is_visible(selectors.menu_no_results, timeout=5)
        except:pass
        result = self.browser.get_element_count(selectors.menu_no_results)
        if result > 0:
            return [{"No results found": "No results found"}]

        start_date = utils.get_month_range(number_of_months)

        list_news = []
        self.browser.wait_until_element_is_visible(selectors.label_page_counts, timeout=30)
        page_count = self.browser.get_text(selectors.label_page_counts)
        page_count = page_count.strip().replace(",", "").split(" ")[-1]

        # Loop through pages
        for j in range(1, int(page_count) + 1):
            logger.info(f"Page {j} of {page_count}")
            self.browser.wait_for_condition('return document.readyState == "complete"', timeout=30)
            self.browser.wait_until_element_is_visible(selectors.menu_search_results, timeout=30)
            results_per_page = self.browser.get_element_count(selectors.menu_search_results)
            
            # Loop through news
            for i in range(1, results_per_page + 1):
                date = self.browser.get_text(selectors.menu_search_results_timestamp.format(count=i))
                title = self.browser.get_text(selectors.menu_search_results_title.format(count=i))
                description = self.browser.get_text(selectors.menu_search_results_description.format(count=i))
                self.browser.wait_until_element_is_visible(selectors.menu_search_results_img.format(count=i), timeout=30)
                img_url = self.browser.get_element_attribute(selectors.menu_search_results_img.format(count=i), "src")
                results_path = utils.download_image(img_url, self.results_path)
                
                date = parser.parse(date, fuzzy=True)
                # checking if the date is within the range
                if date < start_date:
                    return list_news
                
                list_news.append({
                    "title": title,
                    "date": date.strftime('%m/%d/%Y'),
                    "description": description,
                    "img_path": results_path,
                    "qty_phrases": utils.count_phrases(search_phrase, title, description),
                    "contains_money": utils.contains_money(title, description)
                })
            if j == 10:
                break
            self.browser.click_element(selectors.btn_next_page)
            
        return list_news

    @log_decorator
    def mount_output_file(self, search_phrase: str, list_news: list) -> bool:
        """
        Mount output file with search phrase
        Parameters:
        - search_phrase (str): The phrase used for the search.
        - list_news (list): List of news items.

        Returns:
        - bool: True if the output file is successfully mounted, False otherwise.
        """
        sanitized = re.sub(r'[<>:"/\\|?*]', '_', search_phrase)
        sanitized = sanitized.replace(" ", "_")
        if len(sanitized) > 100:
            sanitized = sanitized[:100]
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        df = pd.DataFrame(list_news)
        df.to_excel(os.path.join(self.results_path, f'Results_LATimes_{search_phrase}_{current_time}.xlsx'), index=False)

        return True

