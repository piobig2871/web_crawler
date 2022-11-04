from functionalities import RestClient
from functionalities.scrap_data import Scrapper


class Config:
    """Borg class"""

    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not self.__dict__:
            self.scrapper = Scrapper()
            self.client = RestClient()
