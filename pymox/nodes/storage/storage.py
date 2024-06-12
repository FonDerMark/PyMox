class Storage:
    def __init__(self, connect):
        self.connect = connect
        self.api_urls = {
            'status': '/api2/json/nodes/{node}/storage',
            'content': '/api2/json/nodes/{node}/storage/{storage}/content'
        }

    def get_storage_status(self, node):
        endpoint = self.api_urls['status'].format(node=node)
        return self.connect.get(endpoint)

    def get_content(self, node, storage):
        endpoint = self.api_urls['content'].format(node=node, storage=storage)
        return self.connect.get(endpoint)
