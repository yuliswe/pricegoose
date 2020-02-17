from django.test import RequestFactory, TestCase
from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from src.api.login.google_login import google_login
from src.common.models.user import User
from src.common.models.third_party_users import GoogleUser


class GoogleLoginTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_users_created(self):
        # Create an instance of a POST request.
        request = self.factory.post('/api/login', {'token': 'a_fake_token'})
        # Add a session to the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Make an anonymous user for the request
        request.user = AnonymousUser()

        # User info
        email = 'test@gmail.com'
        fname = 'FirstName'
        lname = 'LastName'
        google_id = 'agoogleid1'

        google_login(request, email, fname, lname, google_id)

        # Check GoogleUser is created
        google_user = GoogleUser.objects.get(sub=google_id)
        self.assertEqual(google_user.sub, google_id)

        # Check User is created
        user = User.objects.get(username=email, email=email, first_name=fname, last_name=lname)
        self.assertEqual(user.username, email)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, fname)
        self.assertEqual(user.last_name, lname)

    # Checks when user updates their information on google, whether User object
    #   is updated correctly
    def test_user_info_updated(self):
        # Create an instance of a POST request.
        request = self.factory.post('/api/login', {'token': 'a_fake_token2'})
        # Add a session to the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Make an anonymous user for the request
        request.user = AnonymousUser()

        # User info
        email = 'test@gmail.com'
        fname = 'FirstName'
        lname = 'LastName'
        google_id = 'agoogleid2'

        # Login with the above user info
        google_login(request, email, fname, lname, google_id)
        logout(request)

        # Modify User Info
        email = 'test2@gmail.com'
        fname = 'FirstName2'
        lname = 'LastName2'

        # Login again with new info
        google_login(request, email, fname, lname, google_id)

        # Check User is updated
        user = User.objects.get(username=email, email=email, first_name=fname, last_name=lname)
        self.assertEqual(user.username, email)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, fname)
        self.assertEqual(user.last_name, lname)

    # Checks when user attemps login while already logged in, it raises exception
    def test_double_login_exception(self):
        # Create an instance of a POST request.
        request = self.factory.post('/api/login', {'token': 'a_fake_token2'})
        # Add a session to the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Make an anonymous user for the request
        request.user = AnonymousUser()

        # User info
        email = 'test@gmail.com'
        fname = 'FirstName'
        lname = 'LastName'
        google_id = 'agoogleid3'

        # Login with the above user info
        google_login(request, email, fname, lname, google_id)

        # Another User Info
        email2 = 'test2@gmail.com'
        fname2 = 'FirstName2'
        lname2 = 'LastName2'
        google_id2 = 'agoogleid4'

        try:
            # Login again
            google_login(request, email2, fname2, lname2, google_id2)

            # Above login should raise exception EnvironmentError
            raise Exception
        except EnvironmentError:
            pass
