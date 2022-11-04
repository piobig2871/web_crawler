from libs.config import Config
import logging
from logging.handlers import StreamHandler


class Log(object):
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        if not self.__shared_state:
            # noinspection PyArgumentList
            log_formatter = logging.Formatter('[%(asctime)s][%(levelname)-7.7s][%(name)-24.24s] %(message)s')
            log_file_handler = StreamHandler() #TODO
            log_file_handler.setFormatter(log_formatter)
            log_console_handler = logging.StreamHandler()
            log_console_handler.setFormatter(log_formatter)
            self._log = logging.getLogger(' scrapper ')
            self._log.addHandler(log_file_handler)
            self._log.addHandler(log_console_handler)
            log_level =
            self._log.setLevel(log_level)
            self._log.info(f"Log level set to: {log_level}")

    @property
    def logger(self):
        return self._log
