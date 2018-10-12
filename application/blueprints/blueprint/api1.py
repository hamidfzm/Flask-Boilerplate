from flask import Blueprint, jsonify

api1 = Blueprint('blueprint.api1', __name__, url_prefix='/api/v1/blueprint')


@api1.route('/hello', methods=['POST'])
def hello():
    return jsonify(hello='world')
