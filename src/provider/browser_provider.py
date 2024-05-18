import os
import sys
from RPA.Browser.Selenium import Selenium

class GenericBrowser:
    def __init__(self):
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
        headless = os.getenv("HEADLESS")
        if headless is None:
            self.options.add_argument("--headless")
    
    def set_options(self, args: list[str] | None):
        self.is_headless()
        self.set_proxy()
        if args:
            for opt in args:
                self.options.add_argument(opt)
            
    def set_proxy(self):
        if os.getenv("PROXY"):
            user = os.getenv("PROXY_USER")
            password = os.getenv("PROXY_PASSWORD")
            url = os.getenv("PROXY")
            port = os.getenv("PROXY_PORT")
            proxy_provider = f'http://{user}:{password}@{url}:{port}'
            self.option.add_argument(f"--proxy-server={proxy_provider}")
    
    def close():
        return self.browser.quit()