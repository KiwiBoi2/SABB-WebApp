# import external libraries
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# create app function
# returns app
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = ")Ld{<oDfg}7^{@WY[r2y<EsQHay6[TEi"

    # import views from views.py
    from .views import views
    # import auth from auth.py
    from .auth import auth

    # register blueprints
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")


    return app