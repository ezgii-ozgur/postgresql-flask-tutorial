from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class StatusHistory(Base):
    __tablename__ = 'StatusHistory'
    _id = Column(String, primary_key=True)

    dcr_version = Column(String)
    device_error_code = Column(Integer)
    device_serial_number = Column(String)
    device_status_code = Column(Integer)
    device_version = Column(String)
    ej_free_space = Column(Integer)
    fiscal_number = Column(String)
    fm_free_space = Column(Integer)
    gprs_ip_address = Column(String)
    merchant_number = Column(Integer)
    not_sent_receipt_count = Column(String)
    software_verification_value = Column(String)
    terminal_date_time = Column(DateTime)
    terminal_id = Column(String)

    created_date = Column(DateTime)
