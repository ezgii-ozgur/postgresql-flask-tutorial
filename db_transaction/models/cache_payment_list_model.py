from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, Integer, Float, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class CachePaymentList(Base):
    __tablename__ = 'CachePaymentList'
    _id = Column(String, primary_key=True)

    acquirer_id = Column(String)
    bank_reference_number = Column(String)
    card_bin = Column(String)
    credit_card_number = Column(String)
    customer_license_plate = Column(String)
    device_serial_number = Column(String)
    device_version = Column(String)
    fiscal_number = Column(String)
    is_cancelled = Column(Boolean)
    island_number = Column(Integer)
    liter = Column(Float)
    merchant_number = Column(Integer)
    paid_amount = Column(Integer)
    payment_id = Column(Integer)
    payment_status = Column(Boolean)
    pos_terminal_id = Column(String)
    product_fuel_type = Column(Integer)
    pump_number = Column(Integer)
    sale_id = Column(Integer)
    slip_text = Column(JSON)
    transaction_date_time = Column(DateTime)
    unit_amount = Column(Float)
    work_time_interval = Column(String)
    created_date = Column(DateTime)
