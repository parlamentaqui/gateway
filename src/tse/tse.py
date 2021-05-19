import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()

ETL_TSE_HOST = os.getenv('ETL_TSE_HOST')
ETL_TSE_PORT = os.getenv('ETL_TSE_PORT')

base_url = f"{ETL_TSE_HOST}:{ETL_TSE_PORT}"

tse = Blueprint('tse', __name__, url_prefix='/tse')

@tse.route('/')
def index():
    return "tse"

@tse.route('/deputies')
def deputies():
    r = requests.get(f'http://{base_url}/api/deputies')
    return r.json()

@tse.route('/get_deputies_equity/<id>')
def get_deputies_equity(id):
    r = requests.get(f'http://{base_url}/api/get_deputies_equity/{id}')
    return jsonify(r.json())

@tse.route('/get_filtered_deputies_equity', methods=['POST'])
def get_filtered_deputies_equity():
    r = requests.post(f'http://{base_url}/api/get_filtered_deputies_equity', json=request.get_json())
    return jsonify(r.json())

@tse.route('/get_total_value_deputies_equity/<id>')
def get_total_value_deputies_equity(id):
    r = requests.get(f'http://{base_url}/api/get_total_value_deputies_equity/{id}')
    return jsonify(r.json())
    
@tse.route('/csv_deputies')
def csv_deputies():
    r = requests.get(f'http://{base_url}/api/csv_deputies')
    return jsonify(r.json())