import connexion
import six

from swagger_server import util

import pymongo
from bson.json_util import dumps
from datetime import datetime

def connect_to_collection(address="mongo", port="27017", db="Client2", col="captures"):
    myclient = pymongo.MongoClient("mongodb://"+address+":"+port+"/")
    mydb = myclient[db]
    mycol = mydb[col]
    return mycol

def get_sensor_captures(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", 1) #tri en descendant
    
    print("All captures for sensor "+sensor_name+": \n"+str(dumps(mydoc, indent=4, sort_keys=True))+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)

def get_last_sensor_capture(mycol=connect_to_collection(), sensor_name="Temperature5"):
    myquery = {"NomCapteur": sensor_name}

    mydoc = mycol.find(myquery).sort("TimestampCapture", -1) #tri en descendant
    
    print("Last capture for sensor "+sensor_name+": \n"+str(mydoc[0])+"\n\n") 
    return dumps(mydoc[0])

def get_avg_in_period(mycol=connect_to_collection(), sensor_name="Temperature5", start=datetime(2019, 9, 1, 00, 00, 00), end=datetime(2020, 1, 1, 00, 00, 00)):

    start_str = start.strftime("%d/%m/%Y %H:%M:%S")
    end_str = end.strftime("%d/%m/%Y %H:%M:%S")
    start = start.timestamp()
    end = end.timestamp()

    pipeline = [
        {
            "$match": {
                "NomCapteur": sensor_name,
                "TimestampCapture": {
                    "$gte": start,
                    "$lt": end
                }  
            }
        },
        {
            "$group": {
                "_id": "$NomCapteur",
                "average": {
                    "$avg": "$ValeurCapture"
                }
            }
        },
        {"$sort": {"TimestampCapture": -1}}
    ]


    mydoc = mycol.aggregate(pipeline)

    print("Average for sensor "+sensor_name+" between dates "+start_str+" and "+end_str+": \n"+dumps(mydoc, indent=4, sort_keys=True)+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)

def get_min_in_period(mycol=connect_to_collection(), sensor_name="Temperature5", start=datetime(2018, 9, 1, 00, 00, 00), end=datetime(2020, 1, 1, 00, 00, 00)):

    start_str = start.strftime("%d/%m/%Y %H:%M:%S")
    end_str = end.strftime("%d/%m/%Y %H:%M:%S")
    start = start.timestamp()
    end = end.timestamp()

    pipeline = [
        {
            "$match": {
                "NomCapteur": sensor_name,
                "TimestampCapture": {
                    "$gte": start,
                    "$lt": end
                }  
            }
        },
        {
            "$group": {
                "_id": "$NomCapteur",
                "min": {
                    "$min": "$ValeurCapture"
                }
            }
        },
        {"$sort": {"TimestampCapture": -1}}
    ]


    mydoc = mycol.aggregate(pipeline)

    print("Minimum for sensor "+sensor_name+" between dates "+start_str+" and "+end_str+": \n"+dumps(mydoc, indent=4, sort_keys=True)+"\n\n") 
    return dumps(mydoc, indent=4, sort_keys=True)


def mean_sensor_id_get(sensor_id, start_date=None, end_date=None):  # noqa: E501
	"""Calculer la moyenne d&#x27;un capteur entre deux dates

	Optional extended description in CommonMark or HTML. # noqa: E501

	:param sensor_id: String Id of the sensor to get
	:type sensor_id: str
	:param start_date: Integer/timestamp of the start date
	:type start_date: int
	:param end_date: Integer/timestamp of the end date
	:type end_date: int

	:rtype: List[int]
	"""

	return get_avg_in_period(sensor_name=sensor_id, start=datetime.fromtimestamp(start_date), end=datetime.fromtimestamp(end_date))
