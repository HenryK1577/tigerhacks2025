import db
import math

collection = db.systems_collection


#Class representing coordinates of a solar system
class SystemNode:
    def __init__(self, coords):
        self.x, self.y, self.z = coords[0], coords[1], coords[2]
        self.connections = []

    def __repr__(self):
        return f"Node({self.x}, {self.y}, {self.z})"

    def __getattribute__(self, name):
        if name in ('x', 'y', 'z'):
            return object.__getattribute__(self, name)
        
    def add_connection(self, other_node):
        if other_node not in self.connections:
            self.connections.append(other_node)

        
    
        

        

    

#Calculate estimated yearly caloric intake based on average weight, height, age, activity factor, as well as # of passengers
#Based on Mifflin-St Jeor Formula for Basic Metabolic Rate, calculating daily caloric requiremnent
def calculate_yearly_drain(n_passengers, mean_weight = 80, mean_height = 180, mean_age = 30, activity_factor = 1.375):
    return (((10 * mean_weight) + (6.25 * mean_weight) - (5 * mean_age) -80) * activity_factor * n_passengers) * 365

#Calculate x, y, z position relative to earth in lightyears
def locate_system_node(system, verbose = False):

    verbose and print(f"locating system node")

    try:
        raw_ra = system["rightascension"]
        raw_dec = system["declination"]
        raw_dist = system["distance"]
        verbose and print(f"raw_ra: {raw_ra} | raw_dec: {raw_dec} | raw_dist:{raw_dist}")
    except:
        return
    
    verbose and print(f"Located system {system['name']}")
    
    #Convert string rightascension to hours, minutes, seconds then to radians
    h, m, s = raw_ra.strip().split()
    h, m, s = float(h), float(m), float(s)
    verbose and print(f"raw_ra becomes {h:.2f} | {m:.2f} | {s:.2f}")
    decimal_hours = h + m / 60 + s / 3600
    ra = math.radians(decimal_hours * 15)

    #Convert string declination to degrees, minutes, seconds then to radians
    sign = -1 if raw_dec.startswith("-") else 1
    deg, m, s = raw_dec.strip().split()
    deg, m, s = abs(float(deg)), float(m), float(s)
    verbose and print(f"raw_dec becomes {deg:.2f} / {m:.2f} / {s:.2f}")
    dec_degrees = deg + m / 60 + s / 3600
    dec = math.radians(dec_degrees * sign)

    dist = float(raw_dist)
    verbose and print(f"raw_dist becomes {dist:.2f}")
    
    sin_dec = math.sin(dec)
    cos_dec = math.cos(dec)
    sin_ra = math.sin(ra)
    cos_ra = math.cos(ra)

    x_pos = dist * cos_dec * cos_ra
    y_pos = dist * cos_dec * sin_ra
    z_pos = dist * sin_dec


    return (x_pos, y_pos, z_pos)

#Populate a list of nodes
def populate_galaxy(verbose = False):
    nodes = []

    for doc in collection.find():
        
        new_sys = doc["system"]
        try:
            x, y, z = locate_system_node(new_sys, verbose)
            nodes.append(SystemNode((x, y, z)))
        except:
            print(f"Failed to locate some system")
                

    return nodes
    
#Get distance between two nodes
def node_dist(a: "SystemNode", b: "SystemNode"):
    return math.sqrt(
        (a.x - b.x)**2 +
        (a.y - b.y)**2 + 
        (a.z - b.z)**2
    )

#Give nodes edges based on max distance
def build_edges(nodes: list, max_distance: float):
    
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            if node_dist(nodes[i], nodes[j]) <= max_distance:
                nodes[i].add_connection(nodes[j])
                nodes[j].add_connection(nodes[i])

