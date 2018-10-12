from flask import Blueprint, jsonify

ajax = Blueprint('blueprint.ajax', __name__, url_prefix='/ajax/blueprint')


@ajax.route('/hello', methods=['POST'])
def hello():
    return jsonify(hello='world')
