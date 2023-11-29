from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.role_model import Role

Base = declarative_base()


class ArkUsers(Base):
    __tablename__ = 'ArkUsers'
    _id = Column(String, primary_key=True)

    email = Column(String)
    is_active = Column(Boolean)
    is_anonymous = Column(Boolean)
    is_authenticated = Column(Boolean)
    language_selection = Column(String)
    last_login_time = Column(DateTime)
    last_name = Column(String)
    name = Column(String)
    password_hash = Column(String)
    profile_img = Column(String)
    role = Column(String)
    user_merchant_list = Column(JSON)
    username = Column(String)
    created_date = Column(DateTime)
