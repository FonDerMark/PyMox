import json
import os
import requests

from .nodes import Nodes


class PyMox:
    def __init__(self, host, username, password, port=8006, session_file='session.json', verify=True):
        self.csrf_token = None
        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.verify = verify
        self.session_file = session_file
        self.session = requests.Session()
        self.api_urls = {
            'ticket': '/api2/json/access/ticket'
        }

        if os.path.exists(self.session_file):
            self.load_session()
        else:
            self.token = self.get_ticket()
            self.save_session()

    def get_ticket(self):
        url = self.api_urls['ticket']
        response = self.session.post(f'https://{self.host}:{self.port}{url}', data={
            'username': self.username,
            'password': self.password
        }, verify=self.verify)
        print(response)
        data = json.loads(response.content)['data']
        self.csrf_token = data['CSRFPreventionToken']
        self.session.headers.update({
            'Cookie': f'PVEAuthCookie={data["ticket"]}',
            'CSRFPreventionToken': self.csrf_token
        })
        return data['ticket']

    def save_session(self):
        with open(self.session_file, 'w') as f:
            session_data = {
                'headers': dict(self.session.headers),
                'cookies': self.session.cookies.get_dict()
            }
            json.dump(session_data, f)

    def load_session(self):
        with open(self.session_file, 'r') as f:
            session_data = json.load(f)
            self.session.headers.update(session_data['headers'])
            requests.utils.add_dict_to_cookiejar(self.session.cookies, session_data['cookies'])

    def request(self, method, endpoint, **kwargs):
        url = f'https://{self.host}:{self.port}{endpoint}'
        response = self.session.request(method, url, verify=self.verify, *kwargs)

        if response.status_code == 401:  # Unauthorized
            self.token = self.get_ticket()
            self.save_session()
            response = self.session.request(method, url, verify=self.verify, **kwargs)

        response.raise_for_status()
        return response.json()

    def get(self, endpoint):
        return self.request('GET', endpoint)

    def post(self, endpoint, data):
        return self.request('POST', endpoint, json=data)

    def delete(self, endpoint):
        return self.request('DELETE', endpoint)

    @property
    def nodes(self):
        return Nodes(session=self)
