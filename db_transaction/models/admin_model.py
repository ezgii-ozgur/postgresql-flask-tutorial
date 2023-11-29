from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean
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
    role_id = Column(ForeignKey(Role.id))  # Role ile ilişkilendirme
    admins = relationship(Role, backref="Admins")

    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine, checkfirst=True)
            Session = sessionmaker(bind=engine)

            session = Session()
            for i in data:
                # role_name = vars(i['role'])['role']
                role_name = i['role']
                existing_role = session.query(Role).filter_by(role=role_name).first()
                if existing_role is not None:
                    role_id = existing_role.id
                    i["role_id"] = role_id
                i.pop('role')
                my_model = Admin(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)
