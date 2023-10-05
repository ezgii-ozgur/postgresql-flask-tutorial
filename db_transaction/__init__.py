from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


db = SQLAlchemy()


def createApp():
    app = Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://username:password@localhost:5432/dbname'
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql://ezgi:123456@localhost:5432/flask-sql"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    db.init_app(app)

    return app
