from django.urls import path
from .views import IndexView

app_name = 'helloworld'

urlpatterns = [
    path('index/', IndexView.as_view()),
]
