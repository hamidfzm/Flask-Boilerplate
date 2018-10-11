from flask_mail import Message

from . import celery, logger
from ..extensions import mail


@celery.task
def send_email(**kwargs):
    message = Message(**kwargs)
    logger.info('Sending email to %s' % message.recipients)
    mail.send(message)
