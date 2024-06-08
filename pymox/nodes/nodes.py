from pymox.request import *
import requests
from .urls import *


class Nodes:
    def __init__(self, connection):
        self.connection = connection
        self.username = connection.username
        self.password = connection.password
        self.host = connection.host
        self.port = connection.port

    def get_nodes(self, node, status):
        if status in ['unknown', 'online', 'offline']:
            data = {
                'node': node,
                'status': status
            }
            response = requests.get(f'http://{self.host}:{self.port}' + nodes_get, data=data)
            print(response)
