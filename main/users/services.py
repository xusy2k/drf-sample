import logging

from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.translation import gettext_lazy as _

log = logging.getLogger(__name__)


def create_welcome_email(user) -> str:
    """
    Create the body of welcome email.
    """
    context = {}

    if user.first_name:
        title = str(_("Welcome %s!") % user.first_name)
        title_h1 = str(_("Welcome <b>%s</b>!") % user.first_name)
    else:
        title = str(_("Welcome!"))
        title_h1 = title
    context["title"] = title
    context["title_h1"] = title_h1

    return render_to_string("emails/welcome.html", context=context)


def send_welcome_email(user) -> bool:
    """
    Send a welcome email to the user.
    """
    try:
        subject = str(_("Welcome to our platform!"))
        from_email = settings.EMAIL_FROM
        send_mail(
            recipient_list=[user.email],
            subject=subject,
            message=create_welcome_email(user),
            from_email=from_email,
            fail_silently=False,
        )
    except Exception as e:  # noqa: BLE001
        log.error(f"Error sending email to {user.email}: {e}")  # noqa: TRY400
        return False
    else:
        return True


def send_welcome_sms(user) -> bool:
    """
    Send a welcome SMS to the user.
    @ToDO: Implement SMS service
    """
    text = _("Welcome to our platform!")
    log.info(f"SMS sent successfully to {user.phone_number} with text: {text}")
    return True
