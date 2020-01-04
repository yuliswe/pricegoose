from .google_login import google_login
from rest_framework.views import APIView
from rest_framework.response import Response


class LoginAPI(APIView):
    def post(self, request):
        try:
            # TODO Currently only handles google login, add more
            google_login(request)
        except KeyError:
            return Response(status=400)
        except:
            return Response(status=400)
            
        return Response(True)