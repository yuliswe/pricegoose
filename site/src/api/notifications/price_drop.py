from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def price_drop_email():
    html_message = render_to_string('email_templates/price_drop.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    subject = 'Price Drop Alert'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_from, ]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message, fail_silently=False)
