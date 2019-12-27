from .google_login import google_login


def user_login(request):
    google_login(request)