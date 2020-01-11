import pymongo
import json



with open('../generated_data.txt') as json_file:
    data = json.load(json_file)

    databases = {}
    connection = pymongo.MongoClient("mongodb://localhost:27017/")

    for client in data:
        databases[client] = {}
        databases[client]["database"] = connection[client]
        databases[client]["capturescol"]  =  databases[client]["database"]["captures"]
        databases[client]["capturescol"].drop() 
        databases[client]["capturescol"]  =  databases[client]["database"]["captures"]

        for room in data[client]:
            for sensor_idx, sensor in enumerate(data[client][room], start=0):
                for capture in data[client][room][sensor_idx]["generated_data"]:
                    document = capture
                    print(document)
                    databases[client]["capturescol"].insert_one(document)
                




print ( connection.list_database_names())
