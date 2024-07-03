from flask import Blueprint, request, jsonify
from app.preprocess import preprocess_data
from app.clustering import cluster_data

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/preprocess', methods=['POST'])
def preprocess():
    data = request.get_json()
    #print('risposta preprocess data',data)
    processed_data = preprocess_data(data)
    return jsonify(processed_data), 200

@bp.route('/cluster', methods=['POST'])
def cluster():
    data = request.get_json()
    #processed_data = preprocess_data(data)
    #clusters = cluster_data(processed_data)
    clusters = cluster_data(data)# TODO da eliminare per la repo definitiva 
    return jsonify(clusters), 200
