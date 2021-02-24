from flask import Blueprint

main = Blueprint('main', __name__)
timer = int()

from . import routes, events
