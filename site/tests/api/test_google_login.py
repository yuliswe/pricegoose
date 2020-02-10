from django.test import RequestFactory, TestCase
from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from src.api.login.google_login import google_login
from src.common.models.user import User
from src.common.models.third_party_users import GoogleUser


class GoogleLoginTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_google_user_created(self):
        # Create an instance of a POST request.
        request = self.factory.post('/api/login', {'token': 'a_fake_token'})
        # Add a session to the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Make an anonymous user for the request
        request.user = AnonymousUser()

        # User info
        email = 'test1@gmail.com'
        fname = 'FirstName1'
        lname = 'LastName1'
        google_id = 'agoogleid1'

        google_login(request, email, fname, lname, google_id)

        google_user, is_created = GoogleUser.objects.get_or_create(sub=google_id)
        self.assertEqual(is_created, False)
        self.assertEqual(google_user.sub, google_id)

    def test_user_created(self):
        # Create an instance of a POST request.
        request = self.factory.post('/api/login', {'token': 'another_fake_token'})
        # Add a session to the request
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()
        # Make an anonymous user for the request
        request.user = AnonymousUser()

        # User info
        email = 'test2@gmail.com'
        fname = 'FirstName2'
        lname = 'LastName2'
        google_id = 'agoogleid2'

        google_login(request, email, fname, lname, google_id)

        user, user_is_created = User.objects.get_or_create(username=email, email=email, first_name=fname, last_name=lname)
        self.assertEqual(user_is_created, False)
        self.assertEqual(user.email, email)
        self.assertEqual(user.first_name, fname)
        self.assertEqual(user.last_name, lname)
