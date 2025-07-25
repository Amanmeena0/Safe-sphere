import os
from flask import Blueprint, request, jsonify
from geopy.distance import geodesic
import json

police_bp = Blueprint("sos", __name__, url_prefix="/sos")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "INDIA_POLICE_STATIONS.geojson")

if not os.path.exists(DATA_PATH):
    raise FileNotFoundError(f"GeoJSON file not found at {DATA_PATH}")

with open(DATA_PATH, "r", encoding="utf-8") as file:
    police_data = json.load(file)

@police_bp.route("/nearest-police-stations", methods=["GET"])
def nearest_police_stations():
    lat = float(request.args.get("lat"))
    lon = float(request.args.get("lon"))
    top = int(request.args.get("top", 3))
    user_location = (lat, lon)
    distances = []

    for feature in police_data["features"]:
        coords = feature["geometry"]["coordinates"]
        station_location = (coords[1], coords[0])  # lat, lon
        distance_km = geodesic(user_location, station_location).kilometers

        distances.append({
            "name": feature["properties"]["ps"],
            "state": feature["properties"]["state"],
            "district": feature["properties"]["district"],
            "coordinates": station_location,
            "distance_km": round(distance_km, 2)
        })

    distances.sort(key=lambda x: x["distance_km"])
    return jsonify(distances[:top])

