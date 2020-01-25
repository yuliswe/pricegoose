from .google_login import google_auth_login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout


class LoginAPI(APIView):
    def post(self, request):
        try:
            # TODO: Currently only handles google login, add more
            google_auth_login(request)
        except KeyError:
            return Response(status=400, data="Error: Login Failed (Code: 10001)")
        except AttributeError:
            return Response(status=400, data="Error: Login Failed (Code: 10002)")
        except EnvironmentError:
            return Response(status=400, data="Error: Login Failed (Code: 10003)")
        except Exception:
            return Response(status=400, data="Error: Login Failed (Code: 10004)")

        return Response(True)


class LogoutAPI(APIView):
    def post(self, request):
        try:
            logout(request)
        except Exception:
            return Response(status=400, data="Error: Login Failed (Code: 10004)")
        return Response(True)
