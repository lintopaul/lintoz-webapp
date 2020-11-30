# This app can read and update user quota comprising of cpu, memory and disk
import json

from flask import Flask, jsonify, request
from waitress import serve

app = Flask(__name__)


# Reads quota from file
# curl http://localhost:8080/get
def read_quota():
    with open('files/quota.json', 'r') as json_in:
        quota = json.load(json_in)
        print("Displays quota:\n")
        return quota


# Displays quota from stored file
@app.route('/get')
def get_quota():
    quota = read_quota()
    return jsonify(quota)


# Adds or Updates quota to file
# curl -H "Content-Type: application/json" -X POST \
# -d '{"user3": "Jane", "cpu3": "500m", "memory3": "2Gi", "disk3": "250Gb"}' http://localhost:8080/post
@app.route('/post', methods=['POST'])
def update_quota():
    with open('files/updated_quota.json', 'w') as json_out:
        quota = read_quota()
        new_quota = request.get_json()
        updated_quota = dict(**quota, **new_quota)
        json.dump(updated_quota, json_out)
    return jsonify(updated_quota)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8080)
