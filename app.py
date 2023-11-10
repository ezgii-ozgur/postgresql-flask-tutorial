from flask import Flask, jsonify
from flask_cors import CORS

from db_transaction import createApp
from db_transaction.initialize_db import createDB
from db_transaction.controllers.admin_controllers import *
from db_transaction.models.admin_model import Admin
# from db_transaction.models.role_model import Role
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.types import Integer, String, DateTime
# from db_transaction.models.admin_model import Role
from db_transaction.models.role_model import Role
# app = createApp()
# createDB()

engine = create_engine('postgresql+psycopg2://postgres:Annem-1979@localhost/postgres', echo=True)

print("engine", engine)
# patent_table = Admin().patent_table
# data = AdminControllers(database_name="Users", collection_name="Admin").get_all_data_in_admin()
# print("data1", data)
# data = [{"role": "admin"}, {"role": "user"}, {"role": "superadmin"}]
data = [{'_id': '62fa1352987387c83c75efbb', 'username': 'ali', 'name': 'Ali', 'email': 'tekin.mertcan@yahoo.com',
         'last_name': 'Tekin', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': False,
         'is_anonymous': False, 'is_authenticated': True, 'role':'admin',
         'profile_img': '_FileServer_Datagenics_2022-12_27-10/ali62f610a26b6929d0489342f9.png',
         'created_date': '12.08.2022 11:34:42'}]
admin1 = Admin.save_db(engine=engine, data=data)
# a = Role.upgrade()

        # {'_id': '62fa1352987387c83c75efbb', 'username': 'mustafa', 'name': 'Mustafa',
        #  'email': 'mustafacnar63@gmail.com', 'last_name': 'çınar', 'password_hash': 'a45958517604f5cd90d6ee51ad9cfdb6',
        #  'is_active': False, 'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2022-12_21-14/mustafa62fa1352987387c83c75efbb.png',
        #  'created_date': '15.08.2022 12:35:14'},
        # {'_id': '62fbec6899fc922b0dc8634c', 'username': 'istanbul_sefiri', 'name': 'Suleyman',
        #  'email': 'deneme@deneme.com', 'last_name': 'Çakır', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e',
        #  'is_active': False, 'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2023-01_10-09/istanbul_sefiri62fbec6899fc922b0dc8634c.png',
        #  'created_date': '16.08.2022 22:13:44'},
        # {'_id': '633be316d06025da15360943', 'username': 'alaca', 'name': 'mustafa',
        #  'email': 'mustafa.alaca@mepsan.com.tr', 'last_name': 'alaca',
        #  'password_hash': '58ae1f97879ab574348b038126e23124', 'is_active': True, 'is_anonymous': False,
        #  'is_authenticated': True, 'role': Role(role= 'user'), 'profile_img': '', 'created_date': '04.10.2022 10:39:02'},
        # {'_id': '637c991014116ebe3b96dbda', 'username': 'tugba.goncu', 'name': 'tuğba',
        #  'email': 'tugbagoncu131@gmail.com', 'last_name': 'göncu', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e',
        #  'is_active': False, 'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2023-01_03-11/tugba.goncu637c991014116ebe3b96dbda.png',
        #  'created_date': '22.11.2022 12:40:32'},
        # {'_id': '6388956208749c5fc8b0a73b', 'username': 'halil', 'name': 'Halil ', 'email': 'halil.rodoplu@hotmail.com',
        #  'last_name': 'Rodoplu', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '01.12.2022 14:52:02'},
        # {'_id': '6389e189c31b9420961cf43c', 'username': 'betul.uslu', 'name': 'betul',
        #  'email': 'betul.uslu@mepsan.com.tr', 'last_name': 'uslu', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e',
        #  'is_active': False, 'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2023-05_26-09/betul.uslu6389e189c31b9420961cf43c.png',
        #  'created_date': '02.12.2022 14:29:13'},
        # {'_id': '63933c3308749c5fc8b0c216', 'username': 'gizem', 'name': 'gizem', 'email': 'gizem.delice@mepsan.com.tr',
        #  'last_name': 'delice', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': False,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2022-12_09-16/gizem63933c3308749c5fc8b0c216.png',
        #  'created_date': '09.12.2022 16:46:27'},
        # {'_id': '63a04e1e25e608427fd23854', 'username': 'busra', 'name': 'büşra', 'email': 'busra.ocal@mepsan.com.tr',
        #  'last_name': 'öçal', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': False,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'),
        #  'profile_img': '_FileServer_Datagenics_2023-06_07-13/busra63a04e1e25e608427fd23854.png',
        #  'created_date': '19.12.2022 14:42:22'},
        # {'_id': '63b41f31ccf172ffbbf94528', 'username': 'ertug', 'name': 'Ertuğ', 'email': 'ertug.erturk@mepsan.com.tr',
        #  'last_name': 'Ertürk', 'password_hash': '58ae1f97879ab574348b038126e23124', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '03.01.2023 15:27:29'},
        # {'_id': '63b41f3fc0de8150e0192f1f', 'username': 'ertug.erturk', 'name': 'ertug',
        #  'email': 'ertug.erturk@mepsan.com.tr', 'last_name': 'erturk',
        #  'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': True, 'is_anonymous': False,
        #  'is_authenticated': True, 'role': 'admin', 'profile_img': '', 'created_date': '03.01.2023 15:27:43'},
        # {'_id': '63eb37d6b98859855cb20ef0', 'username': 'ezgi', 'name': 'Ezgi ', 'email': 'ezgnrzgr@gmail.com',
        #  'last_name': 'Özgür', 'password_hash': 'e58fa828bb3508d72cd4b56464a6c562', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '14.02.2023 10:27:18'},
        # {'_id': '640b406d75576d376ca42320', 'username': 'nagihan.arabaci', 'name': 'Nagihan',
        #  'email': 'nagihan.arabaci@mepsan.com.tr', 'last_name': 'Arabacı',
        #  'password_hash': '58ae1f97879ab574348b038126e23124', 'is_active': True, 'is_anonymous': False,
        #  'is_authenticated': True, 'role': Role(role= 'user'), 'profile_img': '', 'created_date': '10.03.2023 17:36:29'},
        # {'_id': '643d36326f53c8cd8822b1c4', 'username': 'yagmur', 'name': 'yagmur', 'email': 'yagmurbahar-@gmail.com',
        #  'last_name': 'bahar', 'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '17.04.2023 15:06:10'},
        # {'_id': '64589f212c36503c4a415669', 'username': 'selin', 'name': 'selin', 'email': 'selin.kocaer@mepsan.com.tr',
        #  'last_name': 'kocaer', 'password_hash': 'f7058a21f1abf9eacd57b863e4f5bcfe', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '08.05.2023 10:05:05'},
        # {'_id': '6475a00c709d8c238ea45692', 'username': 'meto', 'name': 'metehan',
        #  'email': 'metehan.gokbel@mepsan.com.tr', 'last_name': 'gokbel',
        #  'password_hash': 'e10adc3949ba59abbe56e057f20f883e', 'is_active': True, 'is_anonymous': False,
        #  'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '', 'created_date': '30.05.2023 10:04:44'},
        # {'_id': '64e30d15e656fc533a11245d', 'username': 'eylul', 'name': 'Eylül', 'email': 'eyluloztekin18@gmail.com',
        #  'last_name': 'Öztekin', 'password_hash': 'a256de92cdb1da6beea18efd8056a5f7', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '21.08.2023 10:07:01'},
        # {'_id': '64e30db8805058a0f6356991', 'username': 'mehmet.tilgen', 'name': 'Mehmet ',
        #  'email': 'mehmet.tilgen@mites.local', 'last_name': 'Tilgen',
        #  'password_hash': 'd62692534968a7a7780411ec7d1d9af1', 'is_active': True, 'is_anonymous': False,
        #  'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '', 'created_date': '21.08.2023 10:09:44'},
        # {'_id': '64e30e5980ca9bb21fb49725', 'username': 'ezgigun', 'name': 'ezgi', 'email': 'ezgigun4@gmail.com',
        #  'last_name': 'gun', 'password_hash': '56d78f3e35f4dce96d90a5d751ea8734', 'is_active': True,
        #  'is_anonymous': False, 'is_authenticated': True, 'role': Role(role= 'admin'), 'profile_img': '',
        #  'created_date': '21.08.2023 10:12:25'}]

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
