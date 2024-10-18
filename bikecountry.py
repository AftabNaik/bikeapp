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

# Route to get stations and availability for a specific country and city
@app.route('/network/<country>/<city>', methods=['GET'])
def get_network_by_location(country, city):
    # Fetch all networks
    response = requests.get(CITYBIKES_API_BASE)
    networks = response.json().get('networks', [])

    # Search for a network that matches the provided country and city
    network = next((net for net in networks if net['location']['country'].lower() == country.lower() 
                    and net['location']['city'].lower() == city.lower()), None)

    # If no network is found, return a 404 response
    if not network:
        return jsonify({"error": "Network not found for the specified country and city"}), 404

    # Fetch the specific network data using the network's ID
    network_id = network['id']
    network_response = requests.get(f"{CITYBIKES_API_BASE}/{network_id}")
    network_data = network_response.json()

    return jsonify(network_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
