from subprocess import run
from inspect import getmodule
from pathlib import Path

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings

from ipromise import must_augment


class IntegrationTestCase(StaticLiveServerTestCase):

    fixtures = []

    @must_augment
    def setUp(self):
        raise NotImplementedError

    def __init_subclass__(cls):
        cls.file = getmodule(cls).__file__

        @override_settings(TEST=True)
        def test_runner(self):
            jsf = str(Path(self.file).with_suffix('.js'))
            url = str(self.live_server_url)
            proc = run(['wdio', 'run', 'wdio.headless.conf.js', '--baseUrl', url, '--spec', jsf],
                       cwd=Path(__file__).parent)
            if proc.returncode != 0:
                self.fail(f'Test failed in file "{jsf}"')

        cls.test_runner = test_runner
