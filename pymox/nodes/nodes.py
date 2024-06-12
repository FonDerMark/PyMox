class Nodes:
    def __init__(self, connect):
        self.url = '/api2/json/nodes'
        self.connect = connect
        self.api_urls = {
            'nodes': '/api2/json/nodes',
            'node': '/api2/json/nodes/%s'
        }

    def get_nodes(self, node=None, status=None):
        response = self.connect.get(self.api_urls['nodes'])
        return response

    def get_node(self, node):
        endpoint = (self.api_urls['node'] % node)
        print(endpoint)
        response = self.connect.get(endpoint)
        return response

    def get_lxc(self, node):
    
    
