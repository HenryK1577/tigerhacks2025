from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/project-data")
def project_data():
    user_input = request.args.get("query", "")
    return {"message" : user_input}


if __name__ == "__main__":
    app.run(debug=True)