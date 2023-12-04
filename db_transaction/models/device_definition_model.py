from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceDefinition(Base):
    __tablename__ = 'DeviceDefinition'
    _id = Column(String, primary_key=True)
    definition_status = Column(String)
    device_brand = Column(String)
    device_model = Column(String)
    created_date = Column(DateTime)
