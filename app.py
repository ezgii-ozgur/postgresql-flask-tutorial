from flask import Flask , jsonify
from flask_cors import CORS

from db_transaction import createApp
from db_transaction.initialize_db import createDB
from db_transaction.controllers.admin_controllers import *
from db_transaction.models.admin import Admin

app = createApp()
createDB()

data = AdminControllers(database_name="Prisma",collection_name="Admin").get_all_data_in_admin()

print("1111111111",data)