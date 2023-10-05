from dataclasses import dataclass
from db_transaction import db


@dataclass
class Admin(db.Model):
    __tablename__ = "Admin"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    is_activate = db.Column(db.Boolean, default=True)
    is_anonymous = db.Column(db.Boolean, default=True)
    is_authenticated = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String(120), nullable=False)
    created_date = db.Column(db.Date, default=True)

    def __init__(self, id, username, name, last_name, email, password_hash, is_activate, is_anonymous, is_authenticated,
                 role, image, created_date):
        self.id = id
        self.username = username
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password_hash = password_hash
        self.is_activate = is_activate
        self.is_anonymous = is_anonymous
        self.is_authenticated = is_authenticated
        self.role = role
        self.image = image
        self.created_date = created_date
