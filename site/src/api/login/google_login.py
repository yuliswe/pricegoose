from django.contrib.auth import login
from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed
from src.common.models.user import User
from src.common.models.third_party_users import GoogleUser
from src.api.notifications.welcome import welcome_email
from .token_serializer import TokenSerializer


DEBUG_PRINT = False


'''
    Authenticate the user then log in
'''


def google_auth_login(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data["token"]

    # Authenticate using google_auth, may raise exception
    idinfo = google_auth(token)

    # Unused info for future
    # "email_verified": "true"
    # "name" : "Test User"
    # "picture": "https://lh4.googleusercontent.com/-kYgzyAWpZzJ/ABCDEFGHI/AAAJKLMNOP/tIXL9Ir44LE/s99-c/photo.jpg"
    # "locale": "en"

    # Login using user info in idinfo
    google_login(request, idinfo["email"], idinfo["given_name"], idinfo["family_name"], idinfo["sub"])


'''
    Google OAuth2 Authentication Code
'''

# Constants
CLIENT_ID = "848652265647-3jqp1kq05605bnuj3h7skropcbvqhqhv.apps.googleusercontent.com"
# For testing using Google Playground
# CLIENT_ID = "407408718192.apps.googleusercontent.com"


# Given token, returns user's basic information
# Note: verify_oauth2_token may raise exceptions
def google_auth(token):
    # Specify the CLIENT_ID of the app that accesses the backend:
    idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

    # If token is not issued by google, raise exception
    if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
        raise AuthenticationFailed()

    # ID token is valid. Return the idinfo to caller
    return idinfo


'''
    Login method after successful authentication
    Can be used in unit testing
'''


def google_login(request, email, fname, lname, google_id):
    google_user, is_created = GoogleUser.objects.get_or_create(sub=google_id)
    if DEBUG_PRINT:
        print("Google User has been retrieved or created.")
    if is_created:
        if DEBUG_PRINT:
            print("Creating User.")

        # It's a new user. Create internal User for this user
        user, user_is_created = User.objects.get_or_create(username=email, email=email, first_name=fname, last_name=lname)

        if DEBUG_PRINT:
            print("User has been created.")

        google_user.user = user
        google_user.save()
    else:
        if DEBUG_PRINT:
            print("Existing user, not creating.")

        if google_user.user is None:
            raise AttributeError

        # Update user info
        google_user.user.email = email
        google_user.user.first_name = fname
        google_user.user.last_name = lname
        google_user.save()

        if DEBUG_PRINT:
            print("Existing user info updated.")

    if DEBUG_PRINT:
        print("User and google user set up done.")
    # Send welcome email when user first created
    if is_created:
        welcome_email(email, fname)

    # log in only if user not currently logged in
    if request.user.is_authenticated:
        raise EnvironmentError

    if DEBUG_PRINT:
        print("Logging in the user")
        print(request.user.is_authenticated)

    login(request, google_user.user)

    if DEBUG_PRINT:
        print("Google Login done")
        print(request.user.is_authenticated)
