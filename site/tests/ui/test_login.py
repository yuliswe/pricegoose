
from .base import IntegrationTestCase

from ipromise import augments


class TestLoginLogout(IntegrationTestCase):

    @augments(IntegrationTestCase)
    def setUp(self):
        pass
