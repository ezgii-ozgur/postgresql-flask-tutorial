from sqlalchemy import Column
from sqlalchemy.types import String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefaultValues(Base):
    __tablename__ = 'DefaultValues'
    _id = Column(String, primary_key=True)

    parameter_download_date_time = Column(DateTime)
    receipt_send_time = Column(String)
    sending_status_interval = Column(Integer)
    z_report_send_time = Column(String)
    product_vat_rate = Column(Integer)

    created_date = Column(DateTime)
