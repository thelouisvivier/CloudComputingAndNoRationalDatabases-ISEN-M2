import requests
import json


# Lille request
def get_vlille():
    url = "https://opendata.lillemetropole.fr/api/records/1.0/search/?dataset=vlille-realtime&q=&rows=3000&facet" \
          "=libelle&facet=commune&facet=etat&facet=type&facet=etatconnexion "
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])


# Lyon request (separated in two calls)
def get_vlyon_availability():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_status.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("data", [])
    return data["stations"]


def get_vlyon_geo():
    url = "https://transport.data.gouv.fr/gbfs/lyon/station_information.json"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    data = response_json.get("data", [])
    return data["stations"]


# Rennes request (separated in two calls)
def get_vrennes_geo():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=topologie-des-stations-le-velo-star&q=&facet=codeinseecommune&facet=nomcommune&facet=coordonnees&facet=nombreemplacementstheorique&facet=possedetpe"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])


def get_vrennes_availability():
    url = "https://data.rennesmetropole.fr/api/records/1.0/search/?dataset=etat-des-stations-le-velo-star-en-temps-reel&q=&facet=nom&facet=etat&facet=nombreemplacementsactuels&facet=nombreemplacementsdisponibles&facet=nombrevelosdisponibles"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])


# Paris request
def get_vparis():
    url = "https://opendata.paris.fr/api/records/1.0/search/?dataset=velib-disponibilite-en-temps-reel&q=&facet=name&facet=is_installed&facet=is_renting&facet=is_returning&facet=nom_arrondissement_communes"
    response = requests.request("GET", url)
    response_json = json.loads(response.text.encode('utf8'))
    return response_json.get("records", [])
