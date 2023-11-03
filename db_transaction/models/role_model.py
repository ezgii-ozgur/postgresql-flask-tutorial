from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True)
    role = Column(String)


    @staticmethod
    def save_db(engine, data):
        try:
            Base.metadata.create_all(engine, checkfirst=True)
            Session = sessionmaker(bind=engine)
            session = Session()
            for i in data:
                my_model = Role(**i)
                session.add(my_model)
                session.commit()
        except Exception as ex:
            print("EXXXXXXXXXX",ex)
        # try:
        #     with engine.connect() as conn:
        #         meta_data.create_all(conn, checkfirst=False)
        #         Role.patent_table.create(engine)
        #         for item in data:
        #             print("item", item)
        #             insert_statement = Role.patent_table.insert().values(
        #                 _id=item["_id"],
        #                 role=item["role"]
        #             )
        #             print("insert_statement", insert_statement, type(insert_statement))
        #             conn.execute(insert_statement)
        #             conn.commit()
        #     return True
        # except Exception:
        #     return False
