from db_transaction.utils.data_converter import data_convert_from_cursor_object
from db_transaction.controllers.mongo_client_singleton import MongoRouterClient


class AdminControllers:
    def __init__(self, database_name, collection_name, received_data=None):
        self.database_name = database_name
        self.collection_name = collection_name
        self.received_data = received_data

    def connect_to_mongodb(self):
        mongo_client = MongoRouterClient.get_instance()
        return mongo_client

    def get_all_data_in_admin(self):
        select_db_col = self.connect_to_mongodb()[self.database_name][self.collection_name]
        data = select_db_col.find()
        print("dataaa", data)
        output = data_convert_from_cursor_object(data)

        return output
