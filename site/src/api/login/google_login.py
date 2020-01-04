from django.contrib.auth import login
from .auth.google_auth import google_auth
from .token_serializer import TokenSerializer
from src.common.models.user import User
from src.common.models.google_user import GoogleUser



def google_login(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data["token"]

    # Authenticate using google_auth, may raise exception
    idinfo = google_auth(token)

    # User info
    email = idinfo["email"]
    fname = idinfo["given_name"]
    lname = idinfo["family_name"]
    google_id = idinfo["sub"]
    # Other unused info
    #"email_verified": "true"
    #"name" : "Test User"
    #"picture": "https://lh4.googleusercontent.com/-kYgzyAWpZzJ/ABCDEFGHI/AAAJKLMNOP/tIXL9Ir44LE/s99-c/photo.jpg"
    #"locale": "en"
    
    #google_user, is_created = GoogleUser.objects.get_or_create(google_id)
    #user, created = User.objects.get_or_create(google_user=google_user)
    #user.update(email=email, first_name=fname,last_name=lname)
    user, created = User.objects.get_or_create(email=email, first_name=fname, last_name=lname)

    #user.email=email
    #user.first_name=fname,
    #user.last_name=lname
    #user.save()

    # Send welcome email when user first created
    if created == True:
        ...

    login(request, user)