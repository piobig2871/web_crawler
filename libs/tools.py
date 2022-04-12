from functools import wraps
from http import HTTPStatus
from time import perf_counter

import lxml.html
import requests


def check_if_link_is_alive(url):
	""" Send request and check if web page return status 200. """
	return requests.get(url).status_code == HTTPStatus.OK


def get_links(url):
	""" Debug function, used for refactoring """
	request = requests.get(url=url)
	convert = lxml.html.fromstring(request.content)
	links = convert.xpath('//a/@href')
	return links


def time(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		start = perf_counter()
		_ = function(*args, **kwargs)
		end = perf_counter()
		print(f'Execution time {end - start}')
		return _

	return wrapper


