
from ipromise import overrides
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from . import model_api as a


class SessionModelAPI(a.ModelAPI):
    @property
    @overrides(APIView)
    def permission_classes(self):
        return [IsAuthenticated]

    @property
    def user_lookup_field(self):
        ser_meta = self.get_model_serializer(self.model).Meta
        if hasattr(ser_meta, 'user_lookup_field'):
            return getattr(ser_meta, 'user_lookup_field')
        else:
            raise Exception(f'user_lookup_field does not exist on {ser_meta}, did you forget to define it?')

    @overrides(GenericAPIView)
    def get_queryset(self):
        return super().get_queryset().filter(**{self.user_lookup_field: self.request.user})


class SessionModelObjectAPI(a.ModelObjectAPI, SessionModelAPI):
    @overrides(GenericAPIView)
    def get_queryset(self):
        return a.ModelObjectAPI.get_queryset(self).filter(**{self.user_lookup_field: self.request.user})


class SessionModelFieldAPI(a.ModelFieldAPI, SessionModelAPI):
    @overrides(GenericAPIView)
    def get_queryset(self):
        return a.ModelFieldAPI.get_queryset(self).filter(**{self.user_lookup_field: self.request.user})
