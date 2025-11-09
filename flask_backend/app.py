from flask import Flask, request
from flask_cors import CORS
import db
import core

collection = db.systems_collection
import db

app = Flask(__name__)
CORS(app)

@app.route("/api/planet-data")
def planet_data():
    # Gets user input from the search box and sets it
    # to user_input
    user_input = request.args.get("query", "")
    # find_planet_by_name is used to get the associated json file 
    # and is assinged to data
    data = db.find_planet_by_name(user_input)
    # data is printed to the backend for debugging reasons
    print(data)
    try:
        found_path = core.pathfinder(user_input)
    except:
        print("lol!")

    # data is returned back and formatted
    if found_path:
        return data, found_path
    else:
        return data, "path not found"


if __name__ == "__main__":
    app.run(debug=True)