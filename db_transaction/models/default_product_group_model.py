from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefaultProductGroup(Base):
    __tablename__ = 'DefaultProductGroup'
    _id = Column(String, primary_key=True)

    distributor_company = Column(String)
    fuel_type = Column(String)
    product_fuel_type_code = Column(Integer)
    product_name = Column(String)
    product_order = Column(Integer)
    product_status = Column(Integer)
    product_vat_id = Column(Integer)
    product_vat_rate = Column(Integer)

    created_date = Column(DateTime)
