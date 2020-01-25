from django.urls import path
from .trends import TrendsView

app_name = 'home'

urlpatterns = [
    path('', TrendsView.as_view(), name='trends_view'),
]
