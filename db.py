from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import my_secrets

MONGO_URI = my_secrets.MONGO_URI


#Connect with new client
client = MongoClient(MONGO_URI, server_api = ServerApi('1'))

#Confirm connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

systems_collection = client["celestial_db"]["systems"]

#Find a system by name of the system
def find_system_by_name(system_name, collection = systems_collection):

    system = collection.find_one({"name": {"$regex": f"^{system_name}$", "$options": "i"}})

    if system:
        return {"system": system}
    else:
        return None

#Find a system by name of a star in the system
def find_system_by_star(star_name, collection = systems_collection):

    system = collection.find_one({
        "$or":[
            {"star.name" : {"$regex" :f"^{star_name}$", "$options": "i"}},
            {"binary.name" : {"$regex" :f"^{star_name}$", "$options": "i"}}
        ]
    })

    if system:
        return {"system": system}
    else:
        return None
    
#Find a system by name of a star in the system
def find_system_by_planet(planet_name, collection = systems_collection):
    system = collection.find_one({
        "planet.name": {"regex" : f"^{planet_name}$", "$options": "i"}
    })

    if system:
        return {"system": system}
    else:
        return None