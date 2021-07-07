import configparser
import os
from pathlib import Path

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from flask import Flask
from flask_cors import CORS

from backend.db import dbStructure
from backend.api import BLUEPRINTS

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        ROOT_DIR=os.path.join(app.root_path, '../'),
        SECRET_KEY=os.urandom(24),
        DATABASE=os.path.join(app.instance_path, 'backend.sqlite'),
        UPLOAD_FOLDER=os.path.join(app.root_path, '../files'),
        MAX_CONTETN_LENGTH=5 * 1024 * 1024,
        ALLOWED_EXTENSIONS={'png', 'jpeg', 'jpg', 'gif', 'bmp'},
    )
    CORS(app)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    cfg_parser: configparser.ConfigParser = configparser.ConfigParser()
    cfg_parser.read("backend_config.ini")
    if "Sentry" in cfg_parser.sections():
        sentry_sdk.init(
            cfg_parser["Sentry"]["URI"],
            integrations=[FlaskIntegration(), SqlalchemyIntegration()]
        )

    Path(app.config['UPLOAD_FOLDER']).mkdir(parents=True, exist_ok=True)

    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app
