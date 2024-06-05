from flask import Flask, jsonify
from flask_cors import CORS
import json
import os


json_file_path = os.path.join(os.path.dirname(__file__), 'sample.json')

app = Flask(__name__)
CORS(app)

@app.route('/data', methods=['GET'])
def get_data():
    with open(json_file_path, "r") as f:
        data = f.read()
 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
