import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    from pymongo import MongoClient
    client = MongoClient(os.environ.get("MONGOCONNECTIONSTRING"))

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['SelfServicesBicycle']


def insert_documents(documents, collection):
    dbname = get_database()
    collection_name = dbname[collection]
    collection_name.insert_many(documents)
