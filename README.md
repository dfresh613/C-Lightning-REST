# C-Lightning-REST

(actively in development)

### C-Lightning Rest API wrapper

C-Lightning-REST seeks to be a Lightweight, stable and secure means of accessing your c-lightning node remotely
through a REST API.

C-Lightning-REST works by taking arbirtary commands from an api endpoint `/api/v1/<command>` and attempts to resolve
the command to the corresponding method of PyLightning, execute and return the result in the form of a json response.

Soon to be a plugin of c-lightning

### Configuring

##### Auth
As of now only basic auth is supported. It can be set by configuring the `LN_RPC_USERNAME` and `LN_RPC_PASSWORD` 
environment variables

##### RPC Location of LightningNode
This app must run locally on your LightningNode, the RPC socket location must be set with the `LN_RPC` environment
variable

### Running
    `flask run remotelightning/flaskapp.py`

### Example Query

GET

### Currently Implemented

 - REST API which will forward any command to PyLightning, and respond with the resulting json
 - Basic Authentication

### Soon to be implemented:
  
 - Ability to pass rudimentary arguments and run commands such as invoice
 - TLS support
 - Enable app to run as plugin on c-lightning with prod uwsgi runtime
 
 ### Future Work
 - CORS support for web frameworks
 - local user db, and basic rbac
 - additional auth options
