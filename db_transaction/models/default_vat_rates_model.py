from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefaultVatRates(Base):
    __tablename__ = 'DefaultVatRates'
    _id = Column(String, primary_key=True)
    vat_id = Column(Integer)
    vat_rate = Column(Integer)
    created_date = Column(DateTime)
