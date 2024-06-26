from .lxc import Lxc
from .storage import Storage


class Nodes:
    def __init__(self, session):
        self.session = session
        self.api_urls = {
            'nodes': '/api2/json/nodes',
            'node': '/api2/json/nodes/%s'
        }

    def get_nodes(self, node=None, status=None):
        response = self.session.get(self.api_urls['nodes'])
        return response

    def get_node(self, node):
        endpoint = (self.api_urls['node'] % node)
        print(endpoint)
        response = self.session.get(endpoint)
        return response

    @property
    def lxc(self):
        return Lxc(connect=self.session)

    @property
    def storage(self):
        return Storage(connect=self.session)

