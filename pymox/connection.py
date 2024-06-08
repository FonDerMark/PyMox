from .nodes.nodes import Nodes
from .request import *
from .proxmox_urls import api_urls


class CreateConnection:
    def __init__(self, host,
                 username,
                 password,
                 otp=None,
                 path=None,
                 privs=None,
                 realm=None,
                 tfa_challenge=None,
                 port=8006):
        self.host = host
        self.username = username
        self.password = password
        self.otp = otp
        self.path = path
        self.privs = privs
        self.realm = realm
        self.tfa_challenge = tfa_challenge
        self.port = port
        self.token = None

    @property
    def nodes(self):
        return Nodes(self)

    @property
    def users(self):
        return None

