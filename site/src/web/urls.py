from django.urls import path, include
from src.web.base.views import LogoutView

urlpatterns = [
    path('', include('src.web.home.urls')),
    path('logout', LogoutView.as_view(), name='logout_view'),
]
