from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # すべてのリクエストに対してCORSを有効にする

@app.route('/api/hello', methods=['POST'])
def hello():
    data = request.json
    name = data.get('name')
    return jsonify({
        'message': f'Hello, {name}!'})




if __name__ == '__main__':
    app.run(debug=True)
