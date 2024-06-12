class Lxc:
    def __init__(self, connect):
        self.connect = connect
        self.api_urls = {
            'lxc': '/api2/json/nodes/{node}/lxc'
        }

    def get_lxc(self, node):
        url = self.api_urls['lxc'].format(node=node)
        print(url)
        return self.connect.get(url)

    def os_templates(self):
        pass

    def create_lxc(self, node, ostemplate, vmid):
        pass
