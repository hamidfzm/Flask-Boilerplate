from . import celery, logger


@celery.task
def hello():
    logger.info('Hell from task')
