from django.urls import path, include


urlpatterns = [
    path('helloworld', include('src.api.helloworld.urls')),
]
