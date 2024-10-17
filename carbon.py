from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

CITYBIKES_API_BASE = "https://api.citybik.es/v2/networks"

# Route to get all available bike-sharing networks
@app.route('/networks', methods=['GET'])
def get_networks():
    response = requests.get(CITYBIKES_API_BASE)
    networks = response.json()
    return jsonify(networks)

# Route to get a specific network's stations and availability
@app.route('/network/<network_id>', methods=['GET'])
def get_network_by_id(network_id):
    response = requests.get(f"{CITYBIKES_API_BASE}/{network_id}")
    network = response.json()
    return jsonify(network)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
