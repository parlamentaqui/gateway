from flask import Blueprint

news = Blueprint('news', __name__, url_prefix='/news')

@news.route('/')
def index():
    return "news"