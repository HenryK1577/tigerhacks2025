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

#Use regex to find a system by name of the system
@staticmethod
def find_system_by_name(system_name, collection = systems_collection):

    system = collection.find_one({
        "system.name": {
            "$regex" : f"^{system_name}$",
            "$options": "i"
        }
        })

    if system:
        return {"system": system}
    else:
        return None

#Find a system by name of a star in the system
@staticmethod
def find_system_by_star(star_name, collection = systems_collection):

    system = collection.find_one({
        "system": {
            "$exists" : True
        },

        "$or": [
            #Case 1: Star inside a "binary" container
            {"system.binary.star.name": {"$regex": f"^{star_name}$", "$options": "i"}},

            #Case 2: Star inside a binary INSIDE a binary 
            {"system.binary.binary.star.name": {"$regex": f"^{star_name}$", "$options": "i"}},

            #Case 3: Star directly under system
            {"system.binary.star.name": {"$regex": f"^{star_name}$", "$options": "i"}}
        
            #There are probably exceptions to these three cases
            #Maybe a while loop for nested binaries?
        ]

    })

    if system:
        return {"system": system}
    else:
        return None
    
#Find a system by name of a star in the system
@staticmethod
def find_system_by_planet(planet_name, collection = systems_collection):
    system = collection.find_one({
        "$or": [
            {"system.star.planet.name": {"$regex": f"^{planet_name}$", "$options": "i"}},
            {"system.binary.star.planet.name": {"$regex": f"^{planet_name}$", "$options": "i"}},
            {"system.binary.binary.star.planet.name": {"$regex": f"^{planet_name}$", "$options": "i"}}
        ]
    })

    if system:
        return {"system": system}
    else:
        return None
    


    
#Find a planet by name
@staticmethod
def find_planet_by_name(planet_name, collection = systems_collection):
    system = find_system_by_planet(planet_name)

    def find_in_planet_list(planet_list):
        for planet in planet_list:
            names = planet.get("name")

            if isinstance(names, list): #Some stars have multiple planets
                if any(planet_name.lower() == n.lower() for n in names):
                    return planet
            elif isinstance(names, str): #Some planets have just one star
                if planet_name.lower() == names.lower():
                    return planet
                
        return None


    star_nested = system.get("star", {}).get("planet", [])
    found = find_in_planet_list(star_nested)

    binary_nested = system.get("binary", {}).get("star", {}).get("planet", [])
    found = find_in_planet_list(binary_nested)

    binary_binary_nested = system.get("binary", {}).get("binary", {}).get("star", {})

