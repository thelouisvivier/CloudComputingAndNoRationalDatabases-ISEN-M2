# TP1 - Cloud Computing And No Rational Databases-ISEN-M2

## Prerequeresite
Install requirements via requirements.txt file
```
$ pip install -r requirements.txt
```
Create a .env file with your connection string like that :

```
MONGOCONNECTIONSTRING="mongodb+srv://USERNAME:PASSWORD@CLUSTER"
```

## Client
launch client.py in client folder via
```
$ python client.py
```

## Business
launch business.py in business folder via
```
$ python business.py
```

## More explanation
Our program has a worker which fetch data from the 4 api's (Lille, Rennes, Paris, Lyon) every 1 min. Runs in a thread in client.py.
They are then formatted to get a scheme in order to easier the way of querying back needed data and finally sent ton mongo.
We access our database through a .env file which contains the path.
