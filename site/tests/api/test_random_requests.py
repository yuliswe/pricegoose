
from django.test import Client, TestCase
from django.urls import URLResolver, reverse
from django.urls.exceptions import NoReverseMatch

from src.urls import urlpatterns as base_urlpatterns

CLIENT = Client()

RESP = [
    200,  # ok
    201,  # created
    301,  # moved permanently
    302,  # moved temporarily
    400,  # bad request
    404,  # not found
    403,  # forbidden
    405,  # method not allowed
]


def gen_tests_for_urls(urlpatterns, namespace=[]):

    for urlp in urlpatterns:
        if isinstance(urlp, URLResolver):
            assert urlp.namespace, f'{urlp} has no namespace'
            gen_tests_for_urls(urlp.url_patterns, namespace + [urlp.namespace])
        else:

            class EmptyCase(TestCase):
                pass

            class NonEmptyCase(TestCase):
                def setUp(self):
                    pass

            class NonEmptyLoggedInCase(TestCase):
                def setUp(self):
                    pass

            assert urlp.name, f'{urlp} has no name'

            try:
                url = reverse(':'.join(namespace + [urlp.name]))
            except NoReverseMatch:
                try:
                    url = reverse(':'.join(namespace + [urlp.name]), kwargs={'pk': 1})
                except NoReverseMatch:
                    continue

            def get_tester(self, _url=url):
                resp = CLIENT.get(_url)
                self.assertTrue(resp.status_code in RESP, resp)

            def post_tester(self, _url=url):
                resp = CLIENT.post(_url)
                self.assertTrue(resp.status_code in RESP, resp)

            def patch_tester(self, _url=url):
                resp = CLIENT.patch(_url)
                self.assertTrue(resp.status_code in RESP, resp)

            def delete_tester(self, _url=url):
                resp = CLIENT.delete(_url)
                self.assertTrue(resp.status_code in RESP, resp)

            def put_tester(self, _url=url):
                resp = CLIENT.put(_url)
                self.assertTrue(resp.status_code in RESP, resp)

            classes = {
                f'{namespace}:{urlp.name} (empty)': EmptyCase,
                f'{namespace}:{urlp.name} (nonempty)': NonEmptyCase,
                f'{namespace}:{urlp.name} (nonempty, logged in)': NonEmptyLoggedInCase,
            }

            for testname, clss in classes.items():
                setattr(clss, f'test GET {url}', get_tester)
                setattr(clss, f'test POST {url}', post_tester)
                setattr(clss, f'test PATCH {url}', patch_tester)
                setattr(clss, f'test DELETE {url}', delete_tester)
                setattr(clss, f'test PUT {url}', put_tester)
                globals()[testname] = clss


gen_tests_for_urls(base_urlpatterns)
