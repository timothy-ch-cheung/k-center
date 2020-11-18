import os

import pyutilib.subprocess.GlobalData
from flask import Flask
from flask_cors import CORS

from src.server.incremental_solve import step
from src.server.routes import main

pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False


def create_app():
    app = Flask("__main__", static_folder=f"{os.path.dirname(__file__)}/../../webapp/build/static"
                , template_folder=f"{os.path.dirname(__file__)}/../../webapp/build")
    app.register_blueprint(main)
    app.register_blueprint(step)
    CORS(app)
    return app
