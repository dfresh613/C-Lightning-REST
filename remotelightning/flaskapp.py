from flask import request
from flask import Flask
from .lnrestrouter import CLightningRESTRouter

app = Flask(__name__)
lnrouter = CLightningRESTRouter()
BASE_API_ROUTE = "/api/v1/"
COMMAND_ROUTE = BASE_API_ROUTE+"<command>"


@app.route(COMMAND_ROUTE, methods=["GET", "POST"])
def reroute_parse(command):
    if request.method == "POST":
        cmd_args = gather_args(request)
    else:
        cmd_args = []
    lnrouter.execute_cmd(command, cmd_args)


# TODO Does this ever need to be more complicated? Otherwise remove method
def gather_args(request):
    cmd_args = request.get_json("args", [])
    return cmd_args
