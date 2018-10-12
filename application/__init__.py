from flask import Flask, request

from .tasks import celery
from .config import DefaultConfig


def configure_app(app, configuration=None):
    app.config.from_object(configuration or DefaultConfig)

    app.config.from_pyfile('environ.py', silent=True)
    celery.config_from_object(app.config)


def configure_blueprints(app):
    from . import blueprints

    for blueprint in blueprints.__all__:
        bp = getattr(blueprints, blueprint)
        for route in bp.__all__:
            app.register_blueprint(getattr(bp, route))


def configure_extensions(app):
    from . import extensions
    for extension in extensions.__all__:
        try:
            getattr(extensions, extension).init_app(app)
        except Exception as e:
            raise Exception('Failed to initialize %s. Reason: %s' % (extension, e))


def configure_babel(app):
    with app.app_context():
        from .extensions import babel

        @babel.localeselector
        def get_locale():
            return request.accept_languages.best_match(['en'])


def configure_template_globals(app):
    from .utilities import template_globals

    for name in template_globals.__all__:
        app.add_template_global(getattr(template_globals, name))


def configure_template_filters(app):
    from .utilities import template_filters

    for name in template_filters.__all__:
        func = getattr(template_filters, name)
        app.jinja_env.filters[func.__name__.replace('_filter', '')] = func


def create_app(configuration=None):
    app = Flask(__name__)

    configure_app(app, configuration)
    configure_extensions(app)
    configure_babel(app)
    configure_template_globals(app)
    configure_template_filters(app)
    configure_blueprints(app)

    return app
