from flask import request
from flask import Flask
from flask_basicauth import BasicAuth
import os
from .lnrestrouter import CLightningRESTRouter

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.getenv('LN_API_USER', 'admin')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('LN_API_PASSWORD', 'admin')
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)
lnrouter = CLightningRESTRouter()
BASE_API_ROUTE = "/api/v1/"
COMMAND_ROUTE = BASE_API_ROUTE+"<command>"


@app.route(COMMAND_ROUTE, methods=["GET", "POST"])
def reroute_parse(command):
    if request.method == "POST":
        cmd_args = gather_args(request)
    else:
        cmd_args = []
    return lnrouter.execute_cmd(command, cmd_args)


# TODO Does this ever need to be more complicated? Otherwise remove method
def gather_args(request):
    cmd_args = request.get_json("args", [])
    return cmd_args
