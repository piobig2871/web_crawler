from dataclasses import dataclass
from typing import List

from pages import AbstractPage


@dataclass
class Page(AbstractPage):
    """Page object"""

    def __init__(self, url: str, data: dict, parent: str, subpages: List = []):
        super().__init__(url, data, parent, subpages)
        self._data["url"] = url
        self._data["subpages"] = subpages
        self._data["parent"] = parent
        self._data["status_code"] = None
        self._data["quantity"] = None
        self._data["alive"] = None
        self._data["level"] = None

    @property
    def url(self):
        return self._data["url"]

    @property
    def data(self):
        return self._data["data"]

    @data.setter
    def data(self, value: dict):
        self._data["data"] = value

    @property
    def subpages(self):
        return self._data["subpages"]
