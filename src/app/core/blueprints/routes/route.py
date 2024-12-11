from flask import Blueprint

main = Blueprint("main", __name__)

@main.route("/")
def handle_index():
    return '<h1>Hello World!</h1>'