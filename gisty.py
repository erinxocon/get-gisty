import json

import requests

from datetime import datetime
from typing import Mapping, Dict, Optional, List

BASE_URL = 'https://api.github.com'

MEDIA_TYPE = 'application/vnd.github.v3+json'

session = requests.session()


class File:
    def __init__(self):
        pass


class Gist:

    def __init__(self, gist_dict: Dict) -> None:

        __slots__ = [
            '_url', '_id', '_description', '_public', '_truncated',
            '_comments', '_comments_url', '_html_url', '_git_remote',
            '_created_at', '_updated_at', '_files', '_owner'
            ]

        self._url: str = gist_dict.get('url')
        self._id: str = gist_dict.get('id', None)
        self._description: str = gist_dict.get('description')
        self._public: bool = gist_dict.get('public', True)
        self._truncated: bool = gist_dict.get('truncated', False)
        self._comments: int = gist_dict.get('comments', 0)
        self._comments_url: str = gist_dict.get('comments_url')
        self._html_url: str = gist_dict.get('html_url')
        self._git_remote: str = gist_dict.get('git_push_url')
        self._created_at: str = gist_dict.get('created_at')
        self._updated_at: str = gist_dict.get('updated_at')
        self._files: List[File] = []
        self._owner: str
        try:
            self._owner= gist_dict['owner']['login']
        except KeyError as e:
            self._owner = None


    def __repr__(self):
        return '<Gist id={0}>'.format(self._id)


    @property
    def url(self) -> str:
        return self._url


    @property
    def id(self) -> str:
        return self._id


    @property
    def description(self) -> str:
        return self._description


    @property
    def public(self) -> bool:
        return self._public


    @property
    def truncated(self) -> bool:
        return self._truncated


    @property
    def comments(self) -> int:
        return self._comments


    @property
    def comments_url(self) -> str:
        return self._comments_url


    @property
    def html_url(self) -> str:
        return self._html_url


    @property
    def git_remote(self) -> str:
        return self._git_remote


    @property
    def created_at(self) -> datetime:
        d = datetime.strptime(self._created_at, "%Y-%m-%dT%H:%M:%SZ")
        return d


    @property
    def updated_at(self) -> datetime:
        d = datetime.strptime(self._updated_at, "%Y-%m-%dT%H:%M:%SZ")
        return d


    @property
    def files(self):
        pass


    @property
    def owner(self):
        return self._owner



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
                'Accept': MEDIA_TYPE,
                'Authorization': 'token {0}'.format(self.token)
            }

        return self._headers


    def get_gists(self, username: str = None) -> List[Gist]:
        username = self.username if username is None else username

        url = '{0}/users/{1}/gists'.format(BASE_URL, username)

        r = session.get(url=url, headers=self.headers)

        gist_list: List[Gist] = []

        for g in r.json():
            gist_list.append(Gist(g))

        return gist_list
