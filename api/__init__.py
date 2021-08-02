import os
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from api.db.dbStructure import User
from .db import database as db
from .data import BLUEPRINTS

def create_app(test=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
        ROOT_DIR=os.path.join(app.root_path, '../'),
        TEST_UPLOAD_FOLDER=os.path.join(app.root_path, "../tests/test_files"),
        SECRET_KEY=os.urandom(24),
        DATABASE=os.path.join(app.instance_path, 'backend.sqlite'),
        UPLOAD_FOLDER=os.path.join(app.root_path, '../files'),
        MAX_CONTETN_LENGTH=5 * 1024 * 1024,
        ALLOWED_EXTENSIONS={'png', 'jpeg', 'jpg', 'gif', 'bmp'}
    )
    CORS(app)

    if test is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view('auth.login')
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint)

    return app


if __name__=="__main__":
    app = create_app()
    app.run(debug=False)