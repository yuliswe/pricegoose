from django.contrib.auth import login
from .auth.google_auth import google_auth
from .token_serializer import TokenSerializer
from src.common.models.user import User
from src.common.models.third_party_users import GoogleUser
from src.api.notifications.welcome import welcome_email

DEBUG_PRINT = True

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
    # Other unused info for future
    #"email_verified": "true"
    #"name" : "Test User"
    #"picture": "https://lh4.googleusercontent.com/-kYgzyAWpZzJ/ABCDEFGHI/AAAJKLMNOP/tIXL9Ir44LE/s99-c/photo.jpg"
    #"locale": "en"
    
    google_user, is_created = GoogleUser.objects.get_or_create(sub=google_id)
    if DEBUG_PRINT:
        print("Google User has been retrieved or created.")
    if is_created:
        if DEBUG_PRINT:
            print("Creating User.")

        # It's a new user. Create internal User for this user
        user, user_is_created = User.objects.get_or_create(username=email, email=email, first_name=fname, last_name=lname)
        
        if DEBUG_PRINT:
            print("User has been retrieved or created.")
        
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
    if is_created == True:
        welcome_email(email, fname)

    # TODO fix this since it is not logging in when switching to a new account
    # log in only if user not currently logged in
    if request.user.is_authenticated:
        raise EnvironmentError

    if DEBUG_PRINT:
        print("Logging in the user")

    login(request, user)

    if DEBUG_PRINT:
        print("Google Login done")
    