from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DeviceErrors(Base):
    __tablename__ = 'DeviceErrors'
    _id = Column(String, primary_key=True)
    device_error_queue= Column(JSON)
    fiscal_number= Column(String)
    terminal_date_time= Column(DateTime)
    created_date = Column(DateTime)
