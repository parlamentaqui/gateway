import os
import requests
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

load_dotenv()

ETL_CAMARA_HOST = os.getenv('ETL_CAMARA_HOST')
ETL_CAMARA_PORT = os.getenv('ETL_CAMARA_PORT')

base_url = f"{ETL_CAMARA_HOST}:{ETL_CAMARA_PORT}"

camara = Blueprint('camara', __name__, url_prefix='/camara')

@camara.route('/')
def index():
    return "Camara"

@camara.route('/deputies')
def deputies():
    r = requests.get(f'http://{base_url}/api/deputies')
    return jsonify(r.json())

@camara.route('/home')
def deputies_home():
    r = requests.get(f'http://{base_url}/api/deputies-home')
    return jsonify(r.json())

@camara.route('/resultado', methods=['POST'])
def resultado():
    r = requests.post(f'http://{base_url}/api/resultado', json=request.get_json())
    return jsonify(r.json())

@camara.route('/profile/<id>')
def profile(id):
    r = requests.get(f'http://{base_url}/api/deputies/{id}')
    return r.json()

@camara.route('/parties')
def parties():
    r = requests.get(f'http://{base_url}/api/parties')
    return jsonify(r.json())

@camara.route('/federative_unities')
def federative_unities():
    r = requests.get(f'http://{base_url}/api/federative_unities')
    return jsonify(r.json())

@camara.route('/expenses')
def all_expenses():
    r = requests.get(f'http://{base_url}/api/expenses')

    return jsonify(r.json())

@camara.route('/propositions')
def all_propositions():
    r = requests.get(f'http://{base_url}/api/get_all_propositions')

    return jsonify(r.json())

@camara.route('/expenses/<id>')
def expense(id):
    r = requests.get(f'http://{base_url}/api/expenses/{id}')

    return jsonify(r.json())

@camara.route('/filtered_expenses/<id>', methods=['POST'])
def filtered_expenses(id):
    r = requests.post(f'http://{base_url}/api/filtered_expenses/{id}', json=request.get_json())

    return jsonify(r.json())

@camara.route('/get_votes_by_deputy_id/<id>')
def get_proposition_vote_by_deputy_id(id):
    r = requests.get(f'http://{base_url}/api/get_votes_by_deputy_id/{id}')
    return jsonify(r.json())

@camara.route('/get_proposition_by_id/<id>')
def get_proposition_by_id(id):
    r = requests.get(f'http://{base_url}/api/get_proposition_by_id/{id}')
    return jsonify(r.json())

@camara.route('/get_proposition_by_year/<year>')
def get_proposition_by_year(year):
    r = requests.get(f'http://{base_url}/api/get_proposition_by_year/{year}')
    return jsonify(r.json())
    r = requests.get(f'http://{base_url}/api//get_proposition_by_id/{id}')
    return jsonify(r.json())

@camara.route('/filtered_propositions', methods=['POST'])
def filtered_propositions():
    r = requests.post(f'http://{base_url}/api/filtered_propositions', json=request.get_json())
    return jsonify(r.json())

@camara.route('/deputy_by_name', methods=['POST'])
def deputy_by_name():
    r = requests.post(f'http://{base_url}/api/deputy_by_name', json=request.get_json())
    return jsonify(r.json())
    
@camara.route('/get_propositions_by_author_id/<id>')
def get_propositions_by_author_id(id):
    r = requests.get(f'http://{base_url}/api/get_propositions_by_author_id/{id}')
    return jsonify(r.json())

@camara.route('/get_all_expenses/<id>')
def get_all_expenses(id):
    r = requests.get(f'http://{base_url}/api/expenses/{id}')
    return jsonify(r.json())

@camara.route('/expenses_by_type/<id>')
def expenses_by_type(id):
    r = requests.get(f'http://{base_url}/api/expenses_by_type/{id}')
    return jsonify(r.json())

@camara.route('/get_curiosities_by_id/<id>')
def get_curiosities_by_id(id):
    r = requests.get(f'http://{base_url}/api/get_curiosities/{id}')
    return jsonify(r.json())
  