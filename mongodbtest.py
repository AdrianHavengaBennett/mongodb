import pymongo
# import os

# MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# conn = mongo_connect(MONGODB_URI)
conn = mongo_connect("mongodb+srv://InvAdrian:xxxxxxxxxx@myfirstcluster-e8a5p.mongodb.net/myTestDB?retryWrites=true&w=majority")

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_many({"nationality": "english"}, {"$set": {"occupation": "homeless"}})

documents = coll.find({"nationality": "english"})

for doc in documents:
    print(doc)
