from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


class WelcomeEmailAPI(APIView):
    def post(self, request):
        # TODO: Add user info to email content
        welcome_email()
        return Response(True)


def welcome_email():
    html_message = render_to_string('email_templates/welcome.html', {'context': 'values'})
    plain_message = strip_tags(html_message)
    subject = 'Thank you for registering to our site'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_from,]
    send_mail(subject, plain_message, email_from, recipient_list, html_message=html_message, fail_silently=False)
