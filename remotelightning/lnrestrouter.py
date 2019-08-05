import os
from lightning import LightningRpc


class LNCommandNotFound(Exception):
    def __init__(self):
        pass


# Todo abstract class for use with other daemons if needed
class CLightningRESTRouter(object):

    def __init__(self, rpclocation=None):
        if not rpclocation:
            self.rpclocation = os.getenv('ln_rpc', '~/.lightning/lightning-rpc')
        else:
            self.rpclocation = rpclocation

    def get_connection(self):
        return self._connection

    def _connect(self):
        self._connection = LightningRpc(self.rpclocation)

    lnconn = property(get_connection, _connect)

    def execute_cmd(self, command, cmd_args=[]):
        cmd_result = getattr(self.lnconn, command)
