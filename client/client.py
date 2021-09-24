from threading import Thread
from pymongo import MongoClient

from bicycle_stations_fetcher.database_insert import get_database
from worker.worker import worker

# Attempt start worker to fetch api data every min and populate mongo db
# try:
#    worker = Thread(target=worker)
#    worker.start()
# except:
#    print("Failed to start worker")

# fetch db once
db = get_database()

# Client interaction with data
while True:
    # Get needed infos
    city = input("Enter city (Lille/Paris/Rennes/Lyon) : ")
    long = input("Enter longitude : ")
    lat = input("Enter latitude : ")

    # Recap given parameters
    print("city is: " + city)
    print("long/lat " + long + "/" + lat)

    # Process on mongo and show result
    db.collection.create_index('coordinates', name="2dsphere")
    query = db["fr-lille"].find({
        "coordinates": {
            "$near": {
                "$geometry": {
                    type: "Point",
                    "coordinates": [long, lat]
                },
            }
        }
    })

    for element in query:
        print(element)
