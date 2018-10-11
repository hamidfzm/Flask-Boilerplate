from celery import Celery
from celery.utils.log import get_task_logger

celery = Celery()
logger = get_task_logger(__name__)
