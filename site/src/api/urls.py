from django.urls import path, include
from .login.login import LoginAPI
from .notifications.welcome import WelcomeEmailAPI

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login_api'),
    path('welcome', WelcomeEmailAPI.as_view(), name='welcome_email_api'),
]
