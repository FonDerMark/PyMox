api_urls = {
    'token': {
        'post': {
            'url': '/api2/json/access/ticket',
            'description': 'Create or verify authentication ticket.',
        },

    },
    'lxc': {
        'get': {
            'url': '/api2/json/nodes/{node}/lxc',
            'description': 'LXC container index (per node).',
        },
        'post': {
            'url': '/api2/json/nodes/{node}/lxc',
            'description': 'Create or restore a container.',
        }
    }
}