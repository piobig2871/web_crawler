import requests
import json


class Response:
    """Abstract response"""
    def __init__(self, response: requests.Response):
        try:
            self.content = json.loads(response.text)
        except json.decoder.JSONDecodeError:
            self.content = response.content
        self.headers = response.headers


class RestClient:
    def get(self, url, verify, headers=None):
        """http method for requesting data from the server."""
        return self._request(requests.get, url, verify=verify, headers=headers)

    def post(self, url, content=None, verify=None, headers=None, files=None, data=None ):
        """http method for creating data on the server."""
        return self._request(requests.post, content, verify=verify, headers=headers, files=files, data=data)

    def put(self, url, content=None, verify=None, headers=None, data=None):
        """http method for update data on the server."""
        return self._request(requests.put, url, content, verify=verify, headers=headers, data=data)

    def delete(self, url, content=None, verify=None, headers=None):
        """http method for deleting data from the server."""
        return self._request(requests.delete, url, content, verify=verify, headers=headers)

    def patch(self, url, content=None, verify=None, headers=None):
        """http method for partial update data on the server."""
        return self._request(requests.patch, url, content, verify=verify, headers=headers)

    def _request(self, request, url, content=None, verify=None, headers=None, files=None, data=None):
        """abstract http method"""
        response = request(url, json=content, verify=verify, headers=headers, files=files) if content\
            else request(url, verify=verify, headers=headers, files=files, data=data) if data\
            else request(url, verify=verify, headers=headers, files=files)

        if not response.ok:
            response.reason += 'details: ' + response.text
            response.raise_for_status()

        return Response(response)
