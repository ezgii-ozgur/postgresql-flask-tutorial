from sqlalchemy import Column
from sqlalchemy.types import String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefaultCommunication(Base):
    __tablename__ = 'DefaultCommunication'
    _id = Column(String, primary_key=True)
    csrf_token = Column(String)
    ethernet_ip_1 = Column(String)
    ethernet_ip_2 = Column(String)
    ethernet_port_1 = Column(String)
    ethernet_port_2 = Column(String)
    gprs_ip_1 = Column(String)
    gprs_ip_2 = Column(String)
    gprs_port_1 = Column(String)
    gprs_port_2 = Column(String)
    ntp_ip_1 = Column(String)
    ntp_ip_2 = Column(String)
    ntp_port_1 = Column(String)
    ntp_port_2 = Column(String)
    ssh_ethernet_ip_1 = Column(String)
    ssh_ethernet_ip_2 = Column(String)
    ssh_ethernet_port_1 = Column(String)
    ssh_ethernet_port_2 = Column(String)
    created_date = Column(DateTime)
