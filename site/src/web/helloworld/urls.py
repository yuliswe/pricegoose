from django.urls import path
from .views import IndexView

app_name = 'helloworld'

urlpatterns = [
    path('', IndexView.as_view(), name='index_view'),
]
