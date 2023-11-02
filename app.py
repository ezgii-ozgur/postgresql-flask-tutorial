from flask import Flask, jsonify
from flask_cors import CORS

from db_transaction import createApp
from db_transaction.initialize_db import createDB
from db_transaction.controllers.admin_controllers import *
from db_transaction.models.admin_model import Admin
from db_transaction.models.role_model import Role
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.types import Integer, String, DateTime

# app = createApp()
# createDB()

engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)

print("engine", engine)
meta = MetaData()
# patent_table = Admin().patent_table
# data = AdminControllers(database_name="Prisma", collection_name="Admin").get_all_data_in_admin()
# print("data1", data)
data = [{"_id": 1, "role": "admin"}, {"_id": 2, "role": "user"}, {"_id": 3, "role": "superadmin"}]
admin1 = Admin.save_db(engine=engine, data=data)

# with engine.connect() as conn:
#     patent_table.create(engine)
#     for item in data:
#         print("item", item)
#         # for key, value in item.items():
#         #     print("key ,  value", key, value, type(value))
#         insert_statement = Admin.patent_table.insert().values(
#             _id=item["_id"],
#             username=item["username"],
#             name=item["name"],
#             last_name=item["last_name"],
#             email=item["email"],
#             password_hash=item["password_hash"],
#             is_active=item["is_active"],
#             is_anonymous=item["is_anonymous"],
#             is_authenticated=item["is_authenticated"],
#             created_date=item["created_date"],
#             profile_img=item["profile_img"],
#             role=item["role"]
#             )
#         print("insert_statement",insert_statement, type(insert_statement))
#         conn.execute(insert_statement)
#         conn.commit()
# insert_statement = Admin.patent_table.insert().values(data[0])
# insert_statement = patent_table.insert().values(
#     _id= 1,
#     type='deneme',
#     number=14,
#     name='ezgi'
# )


# import psycopg2
#
# # Establish connection between Redshift and your Python application
# connection = psycopg2.connect(
#     host='localhost',
#     port=5432,
#     user='ezgi',
#     password='123456',
#     database='flask-sql',
# )
# meta = MetaData(connection)
# patent_table = Table("patent",
#                      meta,
#                      Column('_id', Integer),
#                      Column('type', String),
#                      Column('number', Integer),
#                      Column('name', String))
# with connection as conn:
#     patent_table.create()
#     insert_statement = patent_table.insert().values(
#         id= 1,
#         type='deneme',
#         number=14,
#         name='ezgi'
#     )
#     conn.execute(insert_statement)
# # Cursor allows Python to execute PostgreSQL command in a database session
# # What is a cursor? http://initd.org/psycopg/docs/cursor.html
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM deneme;")
# data = cursor.fetchall()
# for row in data:
#     print(row)
# # print(data)
# cursor.close()
# connection.close()
# data = AdminControllers(database_name="Prisma", collection_name="Admin").get_all_data_in_admin()
# print("data ", data, type(data))
# admin1 = Admin(**data[0])
# print("admin1type", type(admin1))
# admin1.add_admin(admin1)
#
# print("1111111111", data)
