from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, JSON, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.terminal_model import Terminal

Base = declarative_base()


class AuthorizedTechnicalService(Base):
    __tablename__ = 'AuthorizedTechnicalService'
    _id = Column(String, primary_key=True)
    authority_end_date= Column(DateTime)
    authority_start_date= Column(DateTime)
    company_code= Column(String)
    company_name= Column(String)
    company_vkn= Column(String)
    device_code= Column(String)
    merchant_number= Column(Integer),
    name_and_lastname= Column(String)
    province_code= Column(String)
    tckn= Column(String)
    created_date = Column(DateTime)
    fk_Terminal_id = Column(ForeignKey(Terminal.id))
    terminals = relationship(Terminal, backref="Terminals")
