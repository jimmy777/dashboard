import sys
import os

from flask.ext.script import Server, Manager
from dashboard.dashboard import app


manager = Manager(app)
server = Server(host="127.0.0.1", port="5050")

manager.add_command("runserver", server)

if __name__ == '__main__':
    manager.run()
