import os
import sys
from RPA.Browser.Selenium import Selenium

class GenericBrowser:
    def __init__(self, headless: bool = True):
        self.options = sys.modules['selenium.webdriver'].ChromeOptions()
        self.default_options = [
            "--no-sandbox",
            "--disable--web-security",
            "--disable-dev-shm-usage",
            "--memory-pressure-off",
            "--ignore-certificate-errors",
            "--disable-notifications",
            "--start-maximized",
            "--disable-logging"
        ]
        self.headless = headless
        self.browser =  self.get_browser()

    def get_browser(self, args: list[str] = None):
        new_args = args
        browser = Selenium()
        if args is None:
            new_args = self.default_options
        self.set_options(new_args)
        return browser
    
    def open_default_browser(self, url: str):   
        self.browser.open_available_browser(url, options=self.options)
        return self.browser
    
    def is_headless(self):
        if self.headless is True:
            self.options.add_argument("--headless")
    
    def set_options(self, args: list[str] | None):
        self.is_headless()
        if args:
            for opt in args:
                self.options.add_argument(opt)
    
    def close():
        return self.browser.quit()