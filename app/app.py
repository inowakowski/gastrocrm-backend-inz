import os
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

from route_config import *


if os.getenv('ENVIRONMENT', 'development') != 'production':
    app.debug = True
CORS(app)

if __name__ == "__main__":
    app.run()
