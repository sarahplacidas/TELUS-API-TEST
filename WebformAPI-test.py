import os
import requests

class TestAPI:

    def setUp(self):
        self.base_url = "https://josephyap9.wixsite.com/qaetestsite"

    def test_get_webform(self):
        """Navigate on QAE site test"""
        response = requests.get(self.base_url)
        assert response["status_code"] == 200