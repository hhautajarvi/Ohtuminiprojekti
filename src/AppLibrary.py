import requests
from initialize_database import initialize_database

class AppLibrary:
    def __init__(self):

        self._base_url = 'http://localhost:5000'

        self.reset_application()

    def reset_application(self):
        initialize_database()

    def create_tip(self, title, author, url, description):
        data = {
            'title': title,
            'author': author,
            'url': url,
            'description':description
        }
        requests.post(f'{self._base_url}/add_tip', data=data)

    def create_user(self, name, username, password):
        data = {
            "name": name,
            "username": username,
            "password": password,
            "password_confirmation": password
        }
        requests.post(f'{self._base_url}/register', data=data)
