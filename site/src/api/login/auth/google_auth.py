from google.oauth2 import id_token
from google.auth.transport import requests
from rest_framework.exceptions import AuthenticationFailed

# Constants
CLIENT_ID = "177658327332-91h4mpna2r7js6hp2hrc79n2vofnorth.apps.googleusercontent.com"

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
