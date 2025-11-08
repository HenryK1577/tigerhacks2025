# Functions related to application core features
import json

class Planet:
    def __init__(self, star_json):
        self.name = star_json["system"]["name" ]
        self.mass = star_json["system"]["star"]["mass"]
        self.radius = star_json["system"]["star"]["radius"]
        self.age = star_json["system"]["star"]["age"]
        self.temperature = star_json["system"]["star"]["temperature"]

# Reads star json data from file
def read_star_json(json_file_path):
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)
    return json_data

# Reads earth data from sun json file
def set_earth_data():
    earth_data = read_star_json('static/Sun.json')
    earth = Planet(earth_data)
    return earth


data = set_earth_data()
print(data.name)
