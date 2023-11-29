# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
# engine = create_engine('sqlite:///veritabani.db')  # Veritabanı bağlantısı
#
# class Role(Base):
#     tablename = 'roles'  # Tablo adını belirtin
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#
# class Admin(Base):
#     tablename = 'admins'  # Tablo adını belirtin
#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     # Diğer sütunlar buraya eklenir
#     role_id = Column(Integer, ForeignKey('roles.id'))
#     role = relationship(Role)
#
# # Veritabanını oluştur
# Base.metadata.create_all(engine)
# # Yeni bir Admin eklemek için
#
# from datetime import datetime
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
# engine = create_engine('sqlite:///veritabani.db')  # Veritabanı bağlantısı
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # Yeni bir rol eklemek için
# admin_role = Role(name='admin')
# session.add(admin_role)
# session.commit()
# # Yeni bir admin eklemek için
# new_admin = Admin(username='busra', name='Büşra', email='busra@', last_name='busra', password_hash='e10adc3949ba59abbe56e057f20f883e', is_active=False, is_anonymous=False, is_authenticated=True, role=admin_role, profile_img='_busra6328524c298585a2c32052da.png', created_date=datetime.now())
# session.add(new_admin)
# session.commit()


# class Category(Base):
#     tablename = "category"
#     id = Column(Integer, primary_key=True, autoincrement="auto")
#     cname = Column(String(255))
#
#     # Relations
#     products = relationship("Product", back_populates="category")
#
#     def repr(self):
#         return f"Category(id={self.id!r}, cname={self.cname!r})"
#
#


from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import event
from datetime import datetime


Base = declarative_base()

class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, Sequence('role_id_seq'), primary_key=True, autoincrement=True)
    role = Column(String)

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
    created_date = Column(DateTime, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(Role.id))
    role = relationship(Role)

def check_and_add_role(mapper, connection, target):
    engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Admin nesnesinin role adını al
    if isinstance(target.role, str):  # Eğer role bir string ise, Role nesnesi oluştur
        role_name = target.role
    else:
        role_name = target.role.role

    # Role tablosunda bu isimde bir rol var mı kontrol et
    existing_role = session.query(Role).filter(Role.role == role_name).first()

    if existing_role is None:
        # Eğer rol yoksa, yeni bir rol ekle
        new_role = Role(role=role_name)
        session.add(new_role)
        session.flush()
        target.role_id = new_role.id  # Yeni rolün id'sini Admin nesnesine ata
    else:
        # Eğer rol varsa, mevcut rolün id'sini Admin nesnesine ata
        target.role_id = existing_role.id# Event'i tanımla
event.listen(Admin, 'before_insert', check_and_add_role)

# Veritabanı bağlantısını oluştur
engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)
Base.metadata.create_all(engine)

# Session oluştur
session = Session(bind=engine)

# Admin ekleyelim

new_admin = Admin(
    _id='some_id',
    username='admin_user',
    role=Role(role='admin')  # Örnek bir rol nesnesi
)

session.add(new_admin)
session.commit()