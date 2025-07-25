from flask import Blueprint, request, jsonify
from app.utils import execute_query
from flask_cors import cross_origin

search_bp = Blueprint('search', __name__)

@search_bp.route("/search", methods=['GET'])
@cross_origin()
def search():
    state_ut = request.args.get('state_ut', '')

    query = "SELECT * FROM crime_data WHERE state_ut LIKE %s"
    params = (f'%{state_ut}%',)
    data = execute_query(query, params)

    
    return jsonify(data), 200



