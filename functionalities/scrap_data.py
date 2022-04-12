from collections import Counter
from http import HTTPStatus
from typing import List

import requests

from libs import Config
from pages.page import Page


class Scrapper(object):
    """Scrapper object which is getting all links, conting them and adding to some shared object (Page structure)"""

    PAGES: List = list()
    INTRODUCE_AS_LINK: List = list()

    def __init__(self, url=None):
        self.url = url
        if not self.url:
            self.__config = Config()
            self.urls = self.__config.get_links()
        else:
            self.__config = Config()
            self.urls = self.__config.get_links(url=self.url)

    def remove_strings(self):
        for url in self.urls:
            if "http" not in url:
                self.urls.remove(url)
                continue
            if "/" not in url:
                self.urls.remove(url)
                continue
            if "@" in url or "mail" in url:
                self.urls.remove(url)
                continue

    def _get_level(self, url):
        return len(self.urls[self.urls.index(url)][8:].split("/"))

    def _get_parent(self, url):
        spl = url[8:].split("/")[:-1]
        return "".join(spl)

    def validate_pages(self) -> List[dict]:
        self.remove_strings()
        counted = dict(Counter(self.urls))
        for _url in counted.keys():
            try:
                try:
                    session = requests.Session()
                    response = session.get(url=_url)
                except requests.exceptions.InvalidSchema:
                    self.urls.remove(_url)
                    continue
                except requests.exceptions.SSLError:
                    self.urls.remove(_url)
                    continue
                Scrapper.PAGES.append(
                    Page(
                        url=_url,
                        data={
                            "status_code": response.status_code,
                            "quantity": counted[_url],
                            "alive": True
                            if response.status_code == HTTPStatus.OK
                            else False,
                            "level": self._get_level(_url),
                        },
                        parent=self._get_parent(_url),
                    )
                )

            except requests.exceptions.MissingSchema:
                Scrapper.INTRODUCE_AS_LINK.append(_url)
                continue
        return Scrapper.PAGES
