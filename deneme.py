from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime ,Uuid
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
# import uuid
#
# Base = declarative_base()
# engine = create_engine('postgresql+psycopg2://ezgi:123456@localhost/flask-sql', echo=True)  # Veritabanı bağlantısı
#
#
# class Role(Base):
#     __tablename__ = 'roles'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
#
# class Admin(Base):
#     __tablename__ = 'admins'
#     id = Column(Uuid, primary_key=True)
#     username = Column(String)
#     name = Column(String)
#     last_name = Column(String)
#     email = Column(String)
#     password_hash = Column(String)
#     is_active = Column(Boolean)
#     is_anonymous = Column(Boolean)
#     is_authenticated = Column(Boolean)
#     profile_img = Column(String)
#     created_date = Column(DateTime)
#     # Diğer sütunlar buraya eklenir
#     role_id = Column(Integer, ForeignKey('roles.id'))  # Role ile ilişkilendirme
#     role = relationship(Role)  # Role tablosu ile ilişki
#
#
# # Veritabanını oluştur
# Base.metadata.create_all(engine, checkfirst=True)
#
# # Yeni bir Admin eklemek için
# from datetime import datetime
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# # engine = create_engine('sqlite:///veritabani.db')  # Veritabanı bağlantısı
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Yeni bir rol eklemek için
# admin_role = Role(name='admin')
# session.add(admin_role)
# session.commit()
#
# # Yeni bir admin eklemek için
# new_admin = Admin(id=uuid.uuid4(),username='busra', name='Büşra', email='busra@', last_name='busra',
#                   password_hash='e10adc3949ba59abbe56e057f20f883e', is_active=False, is_anonymous=False,
#                   is_authenticated=True, role=admin_role, profile_img='_busra6328524c298585a2c32052da.png',
#                   created_date=datetime.now())
# session.add(new_admin)
# session.commit()

from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True)
    role = Column(String)
    # Diğer mevcut sütunlar...
    type = Column(String)  # Yeni kolon ekleniyor

Base.metadata.create_all(engine)
