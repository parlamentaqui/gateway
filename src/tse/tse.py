from flask import Blueprint

tse = Blueprint('tse', __name__, url_prefix='/tse')

@tse.route('/')
def index():
    return "tse"