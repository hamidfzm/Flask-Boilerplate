class DefaultConfig(object):
    DEBUG = True
    TESTING = False
    DEPLOYMENT = False

    SECRET_KEY = 'Development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BABEL_DEFAULT_TIMEZONE = 'UTC'

    UPLOAD_DIR = 'upload'

    TEMPLATES_AUTO_RELOAD = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    EXPLAIN_TEMPLATE_LOADING = False

    RECAPTCHA_PUBLIC_KEY = ''
    RECAPTCHA_PRIVATE_KEY = ''

    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    BROKER_URL = 'redis://localhost:6379/2'
    CELERY_SEND_TASK_SENT_EVENT = True
    CELERY_TIMEZONE = 'UTC'

    MAIL_DEFAULT_SENDER = 'noreply@sender.com'

    PASSWORD_SCHEMES = ('bcrypt',)


class DevelopmentConfig(DefaultConfig):
    TEMPLATES_AUTO_RELOAD = True
    EXPLAIN_TEMPLATE_LOADING = False


class TestConfig(DefaultConfig):
    DEBUG = False
    TESTING = True
    JSONIFY_PRETTYPRINT_REGULAR = False


class DeploymentConfig(DefaultConfig):
    DEBUG = False
    DEPLOYMENT = True
    JSONIFY_PRETTYPRINT_REGULAR = False
