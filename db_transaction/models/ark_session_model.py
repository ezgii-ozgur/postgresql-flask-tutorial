from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.users_model import Users


Base = declarative_base()


class ArkSession(Base):
    __tablename__ = 'ArkSession'
    _id = Column(String, primary_key=True)
    active_jwt_token= Column(String)
    active_token_jti= Column(String)
    cancelled_token_jti= Column(String)
    fk_Users_id= Column(ForeignKey(Users.id))
    ark_sessions = relationship(Users, backref="ArkSessions")
    created_date = Column(DateTime)

