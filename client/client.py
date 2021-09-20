from threading import Thread
from worker.worker import worker

# Attempt start worker to fetch api data every min and populate mongo db
try:
    worker = Thread(target=worker)
    worker.start()
except:
    print("Failed to start worker")

# Client interaction with data
while True:
    # Get needed infos
    city = input("Enter city (Lille/Paris/Rennes/Lyon) : ")
    long = input("Enter longitude : ")
    lat = input("Enter latitude : ")

    # Recap given parameters
    print("city is: " + city)
    print("long/lat " + long + "/" + lat)

    # Process on mongo and sho result
