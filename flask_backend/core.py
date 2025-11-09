# Functions related to application core features
import flask_backend.db as db
import json
import math
from datetime import datetime, timedelta

G_CONSTANT = 6.67430e-11

#Solve Kepler's equation M = E - e*sin(E) for E using Newton-Raphson
def calculate_eccentric_anomaly(mean_anomaly, e, tol=1e-6, max_iter = 100):

    M = mean_anomaly % (2 * math.pi) #Normalize

    #Initial guess
    if e < 0.8:
        E = M
    else:
        E = math.pi

    for i in range(max_iter):
        f = E - e * math.sin(E) - M   #Kepler's equation
        f_prime = 1 - e * math.cos(E) #Derivative

        delta = f / f_prime
        E_next = E - delta

        if abs(delta) < tol:
            return E_next
        
        E = E_next

    print("WARNING: calculate_eccentric_anomaly did not converge")
    return E


#Return's the position of a planet in the solar system relative to the sun.
#Periastron passage based on J2000
def get_solar_planetary_position(planet_name, target_date):
    solar_planets = ["mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
    if planet_name.lower() not in solar_planets:
        raise ValueError("Planet not recognized in solar system")
    else:
        planet = db.find_planet_by_name(planet_name)

    if not isinstance(target_date, (datetime)):
        raise TypeError("target_date is not recognized as datetime.date object")
    
    #Coefficient to turn degrees into radians
    degree_rad_coeff = math.pi / 180
    
    #Various variables essential for calculations
    eccentricity = float(planet["eccentricity"])
    semi_major_axis = float(planet["semimajoraxis"])
    ascending_longitude = float(planet["ascendingnode"]) * degree_rad_coeff
    inclination = float(planet["inclination"]) * degree_rad_coeff
    arg_periapsis = (float(planet["periastron"]) * degree_rad_coeff) - ascending_longitude
    
    #Find time since last periastron passage
    time_periastron = datetime.fromisoformat(planet["lastpassage"])
    t_delta = (target_date - time_periastron).total_seconds() / (24 * 3600) #Convert time delta to days
    
    mean_anomaly = (2 * math.pi) * t_delta
    eccentric_anomaly = calculate_eccentric_anomaly(mean_anomaly, eccentricity)

    true_anomaly = 2 * math.atan((math.sqrt((1+eccentricity)/(1-eccentricity)) * math.tan(eccentric_anomaly / 2)))

    helio_distance = semi_major_axis * (1 - eccentricity * math.cos(eccentric_anomaly))

    #Calculate common expressions just once
    cos_omega = math.cos(ascending_longitude)
    sin_omega = math.sin(ascending_longitude)
    w_plus_v = arg_periapsis + true_anomaly

    #Get X Y Z
    helio_X = helio_distance * (cos_omega * math.cos(w_plus_v) - sin_omega * math.sin(w_plus_v) * math.cos(inclination))
    helio_Y = helio_distance * (sin_omega * math.cos(w_plus_v) + cos_omega * math.sin(w_plus_v) * math.cos(inclination))
    helio_Z = helio_distance * (math.sin(w_plus_v) * math.sin(inclination))

    return (helio_X, helio_Y, helio_Z)













