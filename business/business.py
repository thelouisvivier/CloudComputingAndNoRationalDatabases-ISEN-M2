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
        query = db[city].find({"name": name}).limit(1)

        if len(query) > 0:
            for element in query:
                print(element)
        else:
            print("No result found\n")

    elif action == "update":
        print("update")

    elif action == "delete":
        print("delete")

    elif action == "deactivate":
        print("deactivate")

    else:
        print("Wrong action !")
