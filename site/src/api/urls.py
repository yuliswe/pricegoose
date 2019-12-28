from django.urls import path, include
from .login.login import LoginAPI

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login_api'),
]
