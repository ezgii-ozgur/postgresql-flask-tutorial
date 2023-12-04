from sqlalchemy import Column
from sqlalchemy.types import String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class DefaultGibParameters(Base):
    __tablename__ = 'DefaultGibParameters'
    _id = Column(String, primary_key=True)
    
    daily_sales_report_based_plate_retry= Column(String)
    daily_sales_report_based_plate_retry_interval= Column(String)
    daily_sales_report_retry= Column(String)
    daily_sales_report_retry_interval= Column(String)
    exponantial_rate= Column(String)
    monthly_sales_report_retry= Column(String)
    monthly_sales_report_retry_interval= Column(String)
    pdbs_check_status=Column(String)
    send_daily_sales_report= Column(String)
    send_daily_sales_report_based_on_plate= Column(String)
    send_monthly_sales_report= Column(String)
    send_receipt=Column(String)
    send_receipt_retry= Column(String)
    send_receipt_retry_interval= Column(String)
    send_time_of_daily_sales_report= Column(String)
    send_time_of_daily_sales_report_based_on_plate=Column(String)
    send_time_of_monthly_sales_report= Column(String)
    uptime_connection_without_gib= Column(String)

    created_date = Column(DateTime)
