from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.role_model import Role


Base = declarative_base()


class Admin(Base):
    __tablename__ = 'Admin'
    _id = Column(String, primary_key=True)
    username = Column(String)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password_hash = Column(String)
    is_active = Column(Boolean)
    is_anonymous = Column(Boolean)
    is_authenticated = Column(Boolean)
    profile_img = Column(String)
    created_date = Column(DateTime)
    # Diğer sütunlar buraya eklenir
    role_id = Column(Integer, ForeignKey(Role.id))  # Role ile ilişkilendirme
    role = relationship(Role)  # Role tablosu ile ilişki

    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine, checkfirst=True)
            Session = sessionmaker(bind=engine)

            session = Session()
            for i in data:
                role_name = i['role']
                existing_role = session.query(Role).filter_by(role=role_name).first()

                if existing_role is not None:
                    role_id = existing_role.id
                    i["role_id"] = role_id
                print("i",i)
                my_model = Admin(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)
