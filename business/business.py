from threading import Thread
from pymongo import MongoClient, GEO2D

from bicycle_stations_fetcher.database_insert import get_database
from bicycle_stations_fetcher.get_city import get_city
from worker.worker import worker

# Attempt start worker to fetch api data every min and populate mongo db
# try:
# worker = Thread(target=worker)
# worker.start()
# except:
# print("Failed to start worker")

# fetch db once
db = get_database()
print("find a station with name")
print("update/delete station")
print("deactivate all station in area")
print("give all stations with a ratio bike/total_stand under 20% between 18h and 19h00 (monday to friday)\n")

# Business interaction with data
while True:
    action = input("What to do ? find/update/delete/deactivate :")

    if action == "find":
        city = get_city()
        name = input("Enter name  : ")
        query = db[city].find({"name": name})

        for element in query:
            print(element)

    elif action == "update":
        city = get_city()
        station_id = input("Enter station id  : ")
        query_filter = {"station_id": int(station_id)}
        query = db[city].find(query_filter).limit(1)

        for element in query:
            print(element)

        field = input("Field to update : ")
        update = input("Update with : ")
        new_values = {"$set": {field: update}}
        query_update = db[city].update_one(query_filter, new_values)

    elif action == "delete":
        city = get_city()
        station_id = input("Enter station id  : ")
        query = db[city].delete_many({"station_id": int(station_id)})
        if query.acknowledged:
            print("Entry deleted if exists")
        else:
            print("Failed to delete entry, maybe it doesn't exists")

    elif action == "deactivate":
        city = get_city()
        long = input("Longitude : ")
        lat = input("Latitude : ")
        length = input("Area size (in coordinates precision) : ")

        query = db[city].find({"coordinates": {"$near": [float(long), float(lat)], "$maxDistance": float(length)}})
        to_deactivate = []
        for element in query:
            print("La station " + element['name'] + " va être désactivée")
            to_deactivate.append(element['station_id'])
        for station_id in to_deactivate:
            new_value = {"$set": {'available': False}}
            db[city].update_one({'station_id': station_id}, new_value)



    else:
            print("Wrong action !")
