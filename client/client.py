from threading import Thread

from bicycle_stations_fetcher.database_insert import get_database
from bicycle_stations_fetcher.get_city import get_city

# fetch db once
db = get_database()

# Get needed infos
city = get_city()
long = input("Enter longitude : ")
lat = input("Enter latitude : ")

# Recap given parameters
print("city is: " + city)
print("long/lat " + str(long) + "/" + str(lat))
# Process on mongo and show result
query = db[city].find({"coordinates": {"$near": [float(long), float(lat)]}, "available": True}).limit(3)

print("##########################################")
print("Stations disponibles trouvées près de votre position :")
for element in query:
    print("Nom : " + element["name"])
    print("Adresse : " + element["address"])
    print("Vélos disponibles : " + str(element["available_bikes"]))
    print("Emplacement disponibles : " + str(element["available_slots"]))
    print("TPE : Oui") if element["pos"] else print("TPE : Non")
    print("-------------------------")

