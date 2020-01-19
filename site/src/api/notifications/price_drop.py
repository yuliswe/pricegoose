from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def price_drop_email(recipient, product_name, url):
    html_message = render_to_string('email_templates/price_drop.html',
                                    {'product_name': product_name, 'url': url})
    plain_message = strip_tags(html_message)
    subject = 'Price Drop Alert'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [recipient, ]
    send_mail(subject, plain_message, email_from, recipient_list,
              html_message=html_message, fail_silently=False)
