from django.urls import path, include

urlpatterns = [
    path('', include('src.web.home.urls')),
]
