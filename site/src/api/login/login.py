from .google_login import google_login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout

DEBUG_PRINT = False


class LoginAPI(APIView):
    def post(self, request):
        try:
            # TODO: Currently only handles google login, add more
            google_login(request)
        except KeyError:
            return Response(status=400, data="Error: Login Failed (Code: 10001)")
        except AttributeError:
            return Response(status=400, data="Error: Login Failed (Code: 10002)")
        except EnvironmentError:
            return Response(status=400, data="Error: Login Failed (Code: 10003)")
        except Exception as e:
            if DEBUG_PRINT:
                print(e)
            return Response(status=400, data="Error: Login Failed (Code: 10004)")

        return Response(True)


class LogoutAPI(APIView):
    def post(self, request):
        try:
            if DEBUG_PRINT:
                print("User is being logged out.")
                print(request.user.is_authenticated)
            logout(request)
            if DEBUG_PRINT:
                print("User is logged out.")
                print(request.user.is_authenticated)
        except Exception as e:
            if DEBUG_PRINT:
                print(e)
            return Response(status=400, data="Error: Login Failed (Code: 10004)")
        return Response(True)
