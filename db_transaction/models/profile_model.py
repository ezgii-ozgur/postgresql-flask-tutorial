from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, Integer, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.merchant_model import Merchant

Base = declarative_base()


class Profile(Base):
    __tablename__ = 'Profile'
    _id = Column(String, primary_key=True)

    definition_status = Column(String)
    distributor_company = Column(String)
    epdk_licence_number = Column(String)
    merchant_number = Column(Integer)
    offline_work_duration = Column(String)
    parameter_download_date_time = Column(DateTime)
    profile_name = Column(String)
    profile_status = Column(Integer),
    receipt_header = Column(JSON)
    receipt_sent_time = Column(String)
    send_device_status_interval = Column(Integer)
    send_receipt = Column(Boolean),
    send_z_report = Column(Boolean),
    z_report_sent_time = Column(String)
    created_date = Column(DateTime)

    fk_Merchant_id = Column(ForeignKey(Merchant.id))
    admins = relationship(Merchant, backref="Merchants")
