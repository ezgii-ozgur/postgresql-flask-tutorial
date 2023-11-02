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
    id = Column(Uuid, primary_key=True)
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
            Session = sessionmaker(bind=engine)
            session = Session()
            for i in data:
                session.add(**i)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)
        # try:
        #     with engine.connect() as conn:
        #         meta_data.create_all(conn, checkfirst=False)
        #         Admin.patent_table.create(engine)
        #         # print("aaaaaaaaaaa",a)
        #         for item in data:
        #             print("item", item)
        #             print("_id",item["_id"])
        #             insert_statement = Admin.patent_table.insert().values(
        #                 _id=item["_id"],
        #                 username=item["username"],
        #                 name=item["name"],
        #                 last_name=item["last_name"],
        #                 email=item["email"],
        #                 password_hash=item["password_hash"],
        #                 is_active=item["is_active"],
        #                 is_anonymous=item["is_anonymous"],
        #                 is_authenticated=item["is_authenticated"],
        #                 created_date=item["created_date"],
        #                 profile_img=item["profile_img"],
        #                 role=item["role"]
        #             )
        #             print("insert_statement", insert_statement, type(insert_statement))
        #             conn.execute(insert_statement)
        #         conn.commit()
        #     return True
        # except Exception as ex:
        #     print("exxxxxxxxx", ex)
        #     return False

# @dataclass
# class Admin(db.Model):
#     __tablename__ = "Admin"
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(120), unique=True, nullable=False)
#     name = db.Column(db.String(120), nullable=False)
#     last_name = db.Column(db.String(120), nullable=False)
#     email = db.Column(db.String(120), nullable=False)
#     password_hash = db.Column(db.String(120), nullable=False)
#     is_active = db.Column(db.Boolean, default=True)
#     is_anonymous = db.Column(db.Boolean, default=True)
#     is_authenticated = db.Column(db.Boolean, default=True)
#     role = db.Column(db.String(20), nullable=False)
#     profile_img = db.Column(db.String(120), nullable=False)
#     created_date = db.Column(db.Date, default=True)
#
#     def __init__(self, _id, username, name, last_name, email, password_hash, is_active, is_anonymous, is_authenticated,
#                  role, profile_img, created_date):
#         self._id = _id
#         self.username = username
#         self.name = name
#         self.last_name = last_name
#         self.email = email
#         self.password_hash = password_hash
#         self.is_active = is_active
#         self.is_anonymous = is_anonymous
#         self.is_authenticated = is_authenticated
#         self.role = role
#         self.profile_img = profile_img
#         self.created_date = created_date
#
#         print("111111111111111111111111111",_id)
#
#     @staticmethod
#     def add_admin(model_object):
#         db.session.expunge(model_object)
#         # db.session.add(model_object)
#         # db.session.commit()
#
#     def __repr__(self):
#         print("repr")
#         return (f"{self._id}{self.username}{self.last_name}{self.email}{self.password_hash}{self.is_active}"
#                 f"{self.is_anonymous}{self.is_authenticated}{self.role}{self.profile_img}{self.created_date}")
