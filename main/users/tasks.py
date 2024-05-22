import logging
from typing import TYPE_CHECKING

from django.contrib.auth.models import UserManager as DjangoUserManager

from config import celery_app
from main.common.utils.db_utils import debugger_queries

from .services import send_welcome_email
from .services import send_welcome_sms

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from .models import User


@celery_app.task()
@debugger_queries
def send_email_task(user: DjangoUserManager["User"]):
    return send_welcome_email(user=user)


@celery_app.task()
@debugger_queries
def send_sms_task(user: DjangoUserManager["User"]):
    return send_welcome_sms(user=user)
