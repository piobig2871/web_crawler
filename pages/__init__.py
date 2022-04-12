class AbstractPage:
    def __init__(self, url, data, parent, subpages):
        self._data = {"url": url, "data": data, "parent": parent, "subpages": subpages}

    def __str__(self):
        return f'Page Object: {str(self._data["url"])}'
