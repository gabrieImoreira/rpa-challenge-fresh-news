from src.provider.browser_provider import GenericBrowser
import time
class LATimesCrawler:
    def __init__(self):
        self.browser = GenericBrowser().get_browser()
        self.url = "https://www.latimes.com/"
    
    def main(self):
        pass
        # self.browser.open_available_browser(self.url)
        # time.sleep
        # self.browser.wait_until_page_contains_element("section")
        # self.browser.screenshot("latimes.png")
        # self.browser.close_browser()
        # return self.browser.get_source()
