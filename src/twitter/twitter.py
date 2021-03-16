from flask import Blueprint

twitter = Blueprint('twitter', __name__, url_prefix='/twitter')

@twitter.route('/')
def index():
    return "twitter"