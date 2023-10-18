from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///veritabani.db')  # Veritabanı bağlantısı

class Role(Base):
    tablename = 'roles'  # Tablo adını belirtin
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Admin(Base):
    tablename = 'admins'  # Tablo adını belirtin
    id = Column(Integer, primary_key=True)
    username = Column(String)
    # Diğer sütunlar buraya eklenir
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship(Role)

# Veritabanını oluştur
Base.metadata.create_all(engine)
# Yeni bir Admin eklemek için

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///veritabani.db')  # Veritabanı bağlantısı
Session = sessionmaker(bind=engine)
session = Session()

# Yeni bir rol eklemek için
admin_role = Role(name='admin')
session.add(admin_role)
session.commit()
# Yeni bir admin eklemek için
new_admin = Admin(username='busra', name='Büşra', email='busra@', last_name='busra', password_hash='e10adc3949ba59abbe56e057f20f883e', is_active=False, is_anonymous=False, is_authenticated=True, role=admin_role, profile_img='_busra6328524c298585a2c32052da.png', created_date=datetime.now())
session.add(new_admin)
session.commit()