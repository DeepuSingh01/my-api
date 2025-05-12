from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/")
def index():
    return jsonify({"status": "API is running"})

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(load_data())

@app.route("/add", methods=["POST"])
def add_data():
    new_entry = request.json
    if not new_entry:
        return jsonify({"error": "No data provided"}), 400

    data = load_data()
    data.append(new_entry)
    save_data(data)
    return jsonify({"message": "Data added successfully"}), 201
