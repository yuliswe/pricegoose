
from tests.integration import IntegrationTestCase

from lib.ipromise import augments


class TestLoginLogout(IntegrationTestCase):

    @augments(IntegrationTestCase)
    def setUp(self):
        pass
