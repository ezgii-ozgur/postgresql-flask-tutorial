from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base
from status_history_model import StatusHistory
from sqlalchemy.orm import relationship

Base = declarative_base()


class EventLog(Base):
    __tablename__ = 'EventLog'
    _id = Column(String, primary_key=True)
    cash_register_mode = Column(Integer)
    event_log_date_time = Column(DateTime)
    event_log_type_code = Column(Integer)
    fk_StatusHistory_id = Column(ForeignKey(StatusHistory._id))
    event_logs = relationship(StatusHistory, backref="EventLogs")
    created_date = Column(DateTime)
