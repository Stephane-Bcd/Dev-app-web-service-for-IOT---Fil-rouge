import pymongo

def connect_to_collection(address="localhost", port="27017", db="Client1", col="captures"):
    myclient = pymongo.MongoClient("mongodb://"+address+":"+port+"/")
    mydb = myclient[db]
    mycol = mydb[col]
    return mycol

def get_last_sensor_capture(mycol=connect_to_collection(), sensor_name="Temperature1"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("DateCapture", 1)

    for x in mydoc:
      print(x) 


'''
    TESTS
'''

get_last_sensor_capture()
