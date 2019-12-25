from django.urls import path, include
from .views.index import HelloWorldIndexAPI


urlpatterns = [
    path('', HelloWorldIndexAPI.as_view(), name='index_api'),
]
