import pyutilib.subprocess.GlobalData
from flask import Flask
from flask_cors import CORS

from src.server.routes import main

pyutilib.subprocess.GlobalData.DEFINE_SIGNAL_HANDLERS_DEFAULT = False

app = Flask("__main__", static_folder="../../webapp/build/static", template_folder="../../webapp/build")
app.register_blueprint(main)
CORS(app)

app.run(debug=False, host='0.0.0.0')
