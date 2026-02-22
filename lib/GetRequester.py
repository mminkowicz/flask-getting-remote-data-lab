import requests
import json

class GetRequester:
    """Reusable class for sending HTTP GET requests and parsing JSON responses."""

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send a GET request to the stored URL and return the raw response body."""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """Fetch the response body and parse it as JSON."""
        response_body = self.get_response_body()
        return json.loads(response_body)