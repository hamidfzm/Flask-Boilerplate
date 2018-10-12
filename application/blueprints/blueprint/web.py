from flask import render_template, Blueprint

web = Blueprint('blueprint.web', __name__, url_prefix='/blueprint')


@web.route('/')
def index():
    return render_template('hello.jinja2', hello='world')
