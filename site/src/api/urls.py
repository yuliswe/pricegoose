from django.urls import path
from .login import LoginAPI, LogoutAPI

app_name = 'api'

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login_api'),
    path('logout', LogoutAPI.as_view(), name='logout_api'),
]
