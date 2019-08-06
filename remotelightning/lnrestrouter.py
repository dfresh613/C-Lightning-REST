import json
import os
import copy
from flask import jsonify
from lightning import LightningRpc
from lightning import Millisatoshi


class LNCommandNotFound(Exception):
    def __init__(self):
        pass


# Todo abstract class for use with other daemons if needed
class CLightningRESTRouter(object):

    def __init__(self, rpclocation=None):
        if not rpclocation:
            self.rpclocation = os.getenv('LN_RPC', '~/.lightning/lightning-rpc')
        else:
            self.rpclocation = rpclocation
        self._connection = None

    def get_connection(self):
        if not self._connection:
            self._connect()
        return self._connection

    def _connect(self):
        self._connection = LightningRpc(self.rpclocation)

    lnconn = property(get_connection, _connect)

    def execute_cmd(self, command, cmd_args=[]):
        chosen_cmd = getattr(self.lnconn, command)
        try:
            res = chosen_cmd()
        except FileNotFoundError:
            error = "RPC location does not exist: {}. Be sure to set the LN_RPC environment variable".format(self.rpclocation)
            print(error)
            return jsonify({"message": error}, 500)

        return attempt_jsonify(res), 200


def attempt_jsonify(result):
    try:
        return jsonify(result)
    except TypeError as e:
        result = sanitize_msats(result)
        return jsonify(result)


def sanitize_msats(result):
    """
    Recursive function which sanitizes representation of millisatoshi class so it is jsonifiable
    :param result:
    :return:
    """
    r_dict = copy.deepcopy(result)
    if not hasattr(result, 'items'):
        return result

    for key, value in result.items():
        if isinstance(value, Millisatoshi):
            r_dict[key] = value.millisatoshis
        elif isinstance(value, list):
            sanitized_list = []
            for litem in value:
                sanitized_list.append(sanitize_msats(litem))
            r_dict[key] = sanitized_list
    return r_dict

