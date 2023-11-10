from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey, select, Sequence
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid, Unicode
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from alembic import op
import sqlalchemy as sa

Base = declarative_base()


class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, Sequence('role_id_seq'), primary_key=True, autoincrement=True)
    role = Column(String)


    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            for i in data:
                # role_name = i["role"]
                # existing_role = session.query(Role).filter_by(role=role_name).first()
                # if existing_role is None :
                my_model = Role(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)


