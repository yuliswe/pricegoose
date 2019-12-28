from .google_login import google_login
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginAPI(APIView):
    def post(self, request):
        # TODO Currently only handles google login, add more
        google_login(request)

        return Response()