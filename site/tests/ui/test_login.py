
from .base import IntegrationTestCase

from ipromise import augments


class TestLoginLogout(IntegrationTestCase):

    port = 8080  # required by google auth

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @augments(IntegrationTestCase)
    def setUp(self):
        pass
