from django.http.response import HttpResponseRedirect
from .base_view import BaseView
from django.contrib.auth import logout


class LogoutView(BaseView):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect('/')
