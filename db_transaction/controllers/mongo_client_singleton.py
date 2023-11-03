import pymongo
import os
import datetime

REPLICA_SET_MEMBER1 = os.getenv('REPLICA_SET_MEMBER1_MONGOROUTER_URL')
REPLICA_SET_MEMBER2 = os.getenv('REPLICA_SET_MEMBER2_MONGOROUTER_URL')
REPLICA_SET_MEMBER3 = os.getenv('REPLICA_SET_MEMBER3_MONGOROUTER_URL')

five_hours_added_time = datetime.timedelta(hours=4)


# class MongoRouterClient:
#     __instance = None
#     __connection_uptime = None
#
#     @staticmethod
#     def get_instance():
#         if MongoRouterClient.__instance is None:
#             MongoRouterClient()
#
#         elif (MongoRouterClient.__connection_uptime + five_hours_added_time) < datetime.datetime.now():
#             MongoRouterClient.__instance.close()
#             MongoRouterClient.__instance = pymongo.MongoClient(
#                 f"mongodb://{REPLICA_SET_MEMBER1},{REPLICA_SET_MEMBER2},{REPLICA_SET_MEMBER3}",
#                 connect=False,
#                 serverSelectionTimeoutMS=2000)
#             MongoRouterClient.__connection_uptime = datetime.datetime.now()
#             return MongoRouterClient.__instance
#         return MongoRouterClient.__instance
#
#     def __init__(self):
#         """ Virtually private constructor. """
#
#         if MongoRouterClient.__instance is not None:
#             raise Exception("This class is a singleton!")
#
#         else:
#
#             MongoRouterClient.__instance = pymongo.MongoClient(
#                 f"mongodb://{REPLICA_SET_MEMBER1},{REPLICA_SET_MEMBER2},{REPLICA_SET_MEMBER3}",
#                 connect=False,
#                 serverSelectionTimeoutMS=2000,
#                 replicaSet="ReplicaSetForIMS")
#             MongoRouterClient.__connection_uptime = datetime.datetime.now()



class MongoRouterClient:
    __instance = None
    @staticmethod
    def get_instance():
        if MongoRouterClient.__instance == None:
            MongoRouterClient()
        return MongoRouterClient.__instance
    def __init__(self):
        """ Virtually private constructor. """
        if MongoRouterClient.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            MongoRouterClient.__instance = pymongo.MongoClient("192.168.0.85:27017", connect=False, serverSelectionTimeoutMS=2000)
# ,username=os.getenv('username_root'), password=os.getenv('password_root')