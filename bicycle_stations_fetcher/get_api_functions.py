import requests
import json

# Lille request
from bicycle_stations_fetcher.Station import Station
from bicycle_stations_fetcher.database_insert import insert_documents


def get_lille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet" \
          "=libelle&facet=commune&facet=etat&facet=type&facet=etatconnexion "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("records", [])
    to_insert = []
    for x in data:
        to_insert.append(Station(int(x["fields"]["libelle"]),
                                 x["fields"]["nom"],
                                 x["fields"]["adresse"],
                                 x["fields"]["localisation"][0],
                                 x["fields"]["localisation"][1],
                                 x["fields"]["nbvelosdispo"] + x["fields"]["nbplacesdispo"],
                                 True if x["fields"]["etat"] == "EN SERVICE" else False,
                                 x["fields"]["nbvelosdispo"],
                                 x["fields"]["nbplacesdispo"],
                                 False if x["fields"]["type"] == "SANS TPE" else True).__dict__)
    insert_documents(to_insert, 'fr-lille')


def get_lyon():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_information.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    geo = response_json.get("data", [])
    url2 = "https://transport.data.gouv.fr/gbfs/lyon/station_status.json"
    response2 = requests.request("GET", url2)
    response2_json = json.loads(response2.text.encode('utf8'))
    availability = response2_json.get("data", [])
    to_insert = []
    for x in geo["stations"]:
        y = next((item for item in availability["stations"] if item["station_id"] == x["station_id"]), None)
        to_insert.append(Station(int(x["station_id"]),
                                 x["name"],
                                 x["address"],
                                 x["lat"],
                                 x["lon"],
                                 x["capacity"],
                                 False if (y["is_installed"] == 0 or y["is_renting"] == 0 or y["is_returning"] == 0) else True,
                                 y["num_bikes_available"],
                                 y["num_docks_available"],
                                 None).__dict__)
    insert_documents(to_insert, 'fr-lyon')


# Rennes request
def get_rennes():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=topologie-des-stations-le-velo-star&q" \
          "=&rows=-1&facet=codeinseecommune&facet=nomcommune&facet=coordonnees&facet=nombreemplacementstheorique" \
          "&facet=possedetpe "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    geo = response_json.get("records", [])
    url2 = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps" \
          "-reel&q=&rows=-1&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet" \
          "=nombrevelosdisponibles "
    response2 = requests.request("GET", url2)
    response2_json = json.loads(response2.text.encode('utf8'))
    availability = response2_json.get("records", [])
    to_insert = []
    for x in geo:
        y = next((item for item in availability if item["fields"]["idstation"] == x["fields"]["id"]), None)
        to_insert.append(Station(int(x["fields"]["id"]),
                                 x["fields"]["nom"],
                                 (x["fields"]["adressenumero"] + " " if "adressenumero" in x["fields"] else "") + (x["fields"]["adressevoie"] + ", " if "adressevoie" in x["fields"] else "") + x["fields"]["nomcommune"],
                                 x["fields"]["coordonnees"][0],
                                 x["fields"]["coordonnees"][1],
                                 x["fields"]["nombreemplacementstheorique"],
                                 True if y["fields"]["etat"] == "En fonctionnement" else False,
                                 y["fields"]["nombrevelosdisponibles"],
                                 y["fields"]["nombreemplacementsdisponibles"],
                                 True if x["fields"]["possedetpe"] == "true" else False).__dict__)
    insert_documents(to_insert, 'fr-rennes')


# Paris request
def get_paris():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&rows=-1" \
          "&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("records", [])
    to_insert = []
    for x in data:
        to_insert.append(Station(int(x["fields"]["stationcode"]),
                                 x["fields"]["name"],
                                 x["fields"]["nom_arrondissement_communes"],
                                 x["fields"]["coordonnees_geo"][0],
                                 x["fields"]["coordonnees_geo"][1],
                                 x["fields"]["numdocksavailable"] + x["fields"]["numbikesavailable"],
                                 True if x["fields"]["is_renting"] == "OUI" else False,
                                 x["fields"]["numbikesavailable"],
                                 x["fields"]["numdocksavailable"],
                                 None).__dict__)
    insert_documents(to_insert, 'fr-paris')
