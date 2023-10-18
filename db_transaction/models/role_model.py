from dataclasses import dataclass
# from db_transaction import db
from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, DateTime, Boolean, Uuid
from sqlalchemy.orm import relationship


class Role:
    meta = MetaData()
    patent_table = Table("Role",
                         meta,
                         Column('_id', Integer),
                         Column('role',String,  primary_key=True),
                         schema='public'
                         )
    @staticmethod
    def save_db(engine, data, meta_data):
        try:
            with engine.connect() as conn:
                meta_data.create_all(conn, checkfirst=False)
                Role.patent_table.create(engine)
                for item in data:
                    print("item", item)
                    insert_statement = Role.patent_table.insert().values(
                        _id=item["_id"],
                        role=item["role"]
                    )
                    print("insert_statement", insert_statement, type(insert_statement))
                    conn.execute(insert_statement)
                    conn.commit()
            return True
        except Exception:
            return False
