from flask import Blueprint

camara = Blueprint('camara', __name__, url_prefix='/camara')

@camara.route('/')
def index():
    return "camara!"