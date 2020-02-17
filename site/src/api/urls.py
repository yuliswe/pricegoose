from django.urls import path

from . import model_api as a
from . import session_model_api as s
from .login import LoginAPI, LogoutAPI

app_name = 'api'

urlpatterns = [
    path('login', LoginAPI.as_view(), name='login_api'),
    path('logout', LogoutAPI.as_view(), name='logout_api'),

    path('<str:model>', a.ModelAPI.as_view(), name='model_collection'),
    path('<str:model>/<int:pk>', a.ModelObjectAPI.as_view(), name='model_object'),
    path('<str:model>/<int:pk>/<str:target_field>', a.ModelFieldAPI.as_view(), name='model_field'),

    path('session/<str:model>', s.SessionModelAPI.as_view(), name='session_model_collection'),
    path('session/<str:model>/<int:pk>', s.SessionModelObjectAPI.as_view(), name='session_model_object'),
    path('session/<str:model>/<int:pk>/<str:target_field>', s.SessionModelFieldAPI.as_view(), name='session_model_field'),
]
