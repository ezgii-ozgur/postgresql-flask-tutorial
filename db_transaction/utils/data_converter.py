import json
from bson.objectid import ObjectId
from datetime import datetime


class DataEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        elif isinstance(obj, datetime):
            if obj.year == 1900:
                return obj.strftime("%H:%M")
            else:
                return obj.strftime("%d.%m.%Y %H:%M:%S")

        return json.JSONEncoder.default(self, obj)

def data_convert_from_cursor_object(mongo_data_obj):
    print("aaaaaaaaaaaaa",mongo_data_obj)
    output = []
    for index in mongo_data_obj:
        output.append(json.loads(json.dumps(index, cls=DataEncoder)))
    return output

