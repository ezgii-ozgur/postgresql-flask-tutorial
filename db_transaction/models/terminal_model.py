from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, DateTime, Boolean, Integer, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from db_transaction.models.role_model import Role

Base = declarative_base()


class Terminal(Base):
    __tablename__ = 'Terminal'
    _id = Column(String, primary_key=True)

    certificate_expired_date = Column(String)
    certificate_expired_time = Column(String)
    certificate_initial_date = Column(String)
    certificate_initial_time = Column(String)
    chassis_number = Column(String)
    connection_type = Column(Boolean),
    dcr_id = Column(String)
    definition_status = Column(String)
    deregistration_date_time = Column(DateTime)
    deregistration_for_transfer = Column(Boolean)
    deregistration_status = Column(Boolean)
    device_action_code = Column(Integer)
    device_serial_number = Column(String)
    device_status_code = Column(Integer)
    distributor_firm = Column(String)
    download_communication_data = Column(Boolean)
    download_exchange_rate_data = Column(Boolean)
    download_gib_main_products_data = Column(Boolean)
    download_gib_parameters_data = Column(Boolean),
    download_parameter_details_data = Column(Boolean)
    download_payment_parameters_data = Column(Boolean)
    download_product_group_data = Column(Boolean)
    ej_first_record_date_time = Column(DateTime)
    ej_free_space = Column(Integer)
    ej_last_record_date_time = Column(DateTime)
    epdk_licence_number = Column(String)
    exchange_rate_download_date_time = Column(DateTime)
    firmware_download_date_time = Column(DateTime)
    first_registration_date_time = Column(DateTime)
    first_time_download_parameters = Column(Boolean)
    fiscal_number = Column(String)
    fm_free_space = Column(Integer)
    fm_serial_id = Column(String)
    gib_registration_status = Column(Boolean),
    hardware_version = Column(String)
    imei_number = Column(String)
    instant_message_body = Column(String)
    invoice_date = Column(String)
    invoice_serial_number = Column(Integer)
    is_active = Column(Boolean)
    is_footer_updated = Column(Boolean)
    is_header_updated = Column(Boolean)
    is_scrap = Column(Boolean)
    is_send_gib = Column(Boolean)
    is_transferred = Column(Boolean)
    island_numbers = Column(JSON)
    last_download_date_time = Column(DateTime)
    last_error_code = Column(Integer)
    last_registration_date_time = Column(DateTime)
    merchant_number = Column(Integer)
    okc_public_key = Column(String)
    parameter_download_date_time = Column(DateTime)
    profile_name = Column(String)
    pump_brain = Column(String)
    pump_brand = Column(String)
    pump_model = Column(String)
    receipt_footer = Column(String)
    receipt_header = Column(JSON)
    receipt_send_time = Column(String)
    registration_old_data = Column(Boolean)
    registration_status = Column(Boolean)
    send_receipt = Column(Boolean)
    send_z_report = Column(Boolean)
    sending_status_interval = Column(Integer)
    sim_id = Column(String)
    software_verification_value = Column(String)
    software_version = Column(String)
    station_automation = Column(String)
    terminal_id = Column(String)
    user_password = Column(String)
    z_report_send_time = Column(String)
    created_date = Column(DateTime)
    # Diğer sütunlar buraya eklenir
    fk_Profile_id = Column(ForeignKey(Profile.id))  # Role ile ilişkilendirme
    admins = relationship(Profile, backref="Profile")
