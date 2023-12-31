from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey, select, Sequence, event
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid, Unicode
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from alembic import op
import sqlalchemy as sa

Base = declarative_base()


#DATAGENICS ROLE
class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, Sequence('role_id_seq'), primary_key=True, autoincrement=True)
    role = Column(String, unique=True)


    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            session = Session()
            for i in data:
                my_model = Role(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX", ex)

    @staticmethod
    def check_unique_role_name(mapper, connection, target):
        engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        existing_role = session.query(Role).filter(Role.role == target.role).first()
        if existing_role:
            session.rollback()
            print("Aynı rolle data eklenemez")
            return False


