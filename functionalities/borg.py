from functionalities.scrap_data import Scrapper


class Borg:
	""" Borg class"""
	__shared_state = {}

	def __init__(self):
		self.__dict__ = self.__shared_state
		if not self.__dict__:
			self.scrapper = Scrapper()
