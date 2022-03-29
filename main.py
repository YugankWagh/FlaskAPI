from flask import Flask, jsonify, request
from data import data
#here we creating an app variable
app = Flask(__name__)
#the route / is what the user will open on the browser. whatever we want to return on the browser we will write in the return statement
@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200

@app.route("/planet")
def planet():
    name = request.args.get("name")
    planet_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

if __name__ == "__main__":
    app.run()
    