import json
from typing import List

import lxml.html
import requests


class Config:

    __shared_state = dict()

    PATH_TO_CONFIG = "config.json"
    LINKS = None

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not self.__dict__:
            pass
            # self.scrapper = Scrapper()
            # self.client = RestClient()

    def get_config(self):
        """Pull data from config.json"""
        with open(Config.PATH_TO_CONFIG) as f:
            data = json.load(f)
            if not data:
                print("You have to add config variables to config.json")
        return data

    def get_url(self, url=None) -> str:
        if not url:
            Config.URL = self.get_config()["url"]
        else:
            Config.URL = url
        return Config.URL

    def get_web_page(self, url=None):
        """Request get method for web page content"""
        if not url:
            return requests.get(url=self.get_url())
        else:
            try:
                return requests.get(url=self.get_url(url=url))
            except requests.exceptions.MissingSchema:
                return requests.get(url=self.get_config()["url"] + url)

    def convert_page_to_string(self, url=None) -> str:
        """Convert Response object to python strings"""
        if not url:
            return lxml.html.fromstring(self.get_web_page().content)
        else:
            return lxml.html.fromstring(self.get_web_page(url=url).content)

    def get_links(self, url=None) -> List:
        """Separating links from html content"""
        if not url:
            Config.LINKS = self.convert_page_to_string().xpath("//a/@href")
        else:
            Config.LINKS = self.convert_page_to_string(url=url).xpath("//a/@href")
        return Config.LINKS
