from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/project-data")
def project_data():
    user_input = request.args.get("query", "")
    # my_info = get_data()
    return {my_info}


if __name__ == "__main__":
    app.run(debug=True)