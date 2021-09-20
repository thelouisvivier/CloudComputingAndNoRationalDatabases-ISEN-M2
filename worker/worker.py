import time

from bicycle_stations_fetcher.get_api_functions import *


# Fetch data from wanted endpoint and populate mongo DB
def send_to_mongo(city):
    if city == "Lille":
        print("Fetching Lille...")
        json = get_vlille()
        # now send it
        print("Successfully fetched and moved to mongo")

    elif city == "Paris":
        print("Fetching Paris...")
        json = get_vparis()
        # now send it
        print("Successfully fetched and moved to mongo")

    elif city == "Rennes":
        print("Fetching Rennes...")
        json_geo = get_vrennes_geo()
        json_availability = get_vrennes_availability
        # now send it
        print("Successfully fetched and moved to mongo")

    elif city == "Lyon":
        print("Fetching Lyon...")
        json_geo = get_vlyon_availability
        json_availability = get_vlyon_geo
        # now send it
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
