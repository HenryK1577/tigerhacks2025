from flask import Flask, request
from flask_cors import CORS
import db

collection = db.systems_collection

app = Flask(__name__)
CORS(app)

@app.route("/api/project-data")
def project_data():
    user_input = request.args.get("query", "")
    found_name = db.search_all(user_input)
    if found_name:
        return {"message" : found_name}
    else:
        return{"message" : "System/planet not found"}


if __name__ == "__main__":
    app.run(debug=True)