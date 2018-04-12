import json

import requests

from typing import Mapping, Dict, Optional

BASE_URL = 'https://api.github.com'

MEDIA_TYPE = 'application/vnd.github.v3+json'


class Gist:

    def __init__(self, **kwargs) -> None:
        pass


class Gists:

    def __init__(self, user: str, token: str) -> None:
        self._headers: Dict[str,str] = None
        self._username: str = user
        self._token: str = token



    @property
    def username(self) -> str:
        return self._username


    @property
    def token(self) -> str:
        return self._token


    @property
    def headers(self) -> Dict[str,str]:
        if self._headers is None:
            self._headers = {
                'Accept': 'application/vnd.github.v3+json',
                'Authorization': 'token {0}'.format(self.token)
            }

        return self._headers


    def get_gists(self, username: str = None):
        username = self.username if username is None else username
        url = '{0}/users/{1}/gists'.format(BASE_URL, username)
        r = requests.get(url=url, headers=self.headers)
        return r.json()[0]['files']
