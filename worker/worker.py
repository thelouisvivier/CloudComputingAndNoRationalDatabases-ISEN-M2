import time

from bicycle_stations_fetcher.get_api_functions import *


# Fetch data from wanted endpoint and populate mongo DB
def send_to_mongo(city):
    if city == "Lille":
        print("Fetching Lille...")
        get_lille()
        print("Successfully fetched and moved to mongo")

    elif city == "Paris":
        print("Fetching Paris...")
        get_paris()
        print("Successfully fetched and moved to mongo")

    elif city == "Rennes":
        print("Fetching Rennes...")
        get_rennes_geo()
        get_rennes_availability()
        print("Successfully fetched and moved to mongo")

    elif city == "Lyon":
        print("Fetching Lyon...")
        get_lyon_availability()
        get_lyon_geo()
        print("Successfully fetched and moved to mongo")

    else:
        print("Wrong city endpoint given")
        print("Received : " + city)


# worker wich process given city endpoints
def worker():
    print("worker started")
    while True:
        print("######################")
        send_to_mongo("Lille")
        send_to_mongo("Paris")
        send_to_mongo("Rennes")
        send_to_mongo("Lyon")
        print("######################")
        time.sleep(60)  # wait 1 min
