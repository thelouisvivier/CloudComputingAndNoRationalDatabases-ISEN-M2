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


# Lyon request (separated in two calls)
def get_lyon_availability():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_status.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("data", [])
    return data["stations"]


def get_lyon_geo():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_information.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("data", [])
    to_insert = []
    for x in data["stations"]:
        to_insert.append(Station(int(x["station_id"]),
                                 x["name"],
                                 x["address"],
                                 x["lat"],
                                 x["lon"],
                                 x["capacity"],
                                 False,
                                 0,
                                 x["capacity"],
                                 False).__dict__)
    insert_documents(to_insert, 'fr-lyon')


# Rennes request (separated in two calls)
def get_rennes_geo():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=topologie-des-stations-le-velo-star&q" \
          "=&facet=codeinseecommune&facet=nomcommune&facet=coordonnees&facet=nombreemplacementstheorique&facet" \
          "=possedetpe "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("records", [])
    to_insert = []
    for x in data:
        to_insert.append(Station(int(x["fields"]["id"]),
                                 x["fields"]["nom"],
                                 x["fields"]["adressenumero"] if x["fields"]["adressenumero"] is not None else "" + " " + x["fields"]["adressevoie"] + ", " + x["fields"]["nomcommune"],
                                 x["fields"]["coordonnees"][0],
                                 x["fields"]["coordonnees"][1],
                                 x["fields"]["nombreemplacementstheorique"],
                                 None,
                                 None,
                                 None,
                                 True if x["fields"]["possedetpe"] == "true" else False).__dict__)
    insert_documents(to_insert, 'fr-rennes')


def get_rennes_availability():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps" \
          "-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet" \
          "=nombrevelosdisponibles "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])


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
