from .google_login import google_login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout


class LoginAPI(APIView):
    def post(self, request):
        try:
            # Log Out current user if anyone is logged in
            #if request.user.is_authenticated:
            #    print("already logged in as a user, log out first")
            #    logout(request)

            # TODO: Currently only handles google login, add more
            google_login(request)
        except KeyError:
            return Response(status=400, data="Error: Login Failed (Code: 10001)")
        except AttributeError:
            return Response(status=401, data="Error: Login Failed (Code: 10002)")
        except EnvironmentError:
            return Response(status=402, data="Error: Login Failed (Code: 10003)")
        except:
            return Response(status=403, data="Error: Login Failed (Code: 10004)")
            
        return Response(True)


class LogoutAPI(APIView):
    def post(self, request):
        logout(request)
        return Response(True)
