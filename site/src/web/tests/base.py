from subprocess import run
from inspect import getmodule
from pathlib import Path

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings

from ipromise import must_augment


class IntegrationTestCase(StaticLiveServerTestCase):

    # fixtures = ['tests/integration/testdata.json']

    @must_augment
    def setUp(self):
        raise NotImplementedError

    def __init_subclass__(cls, *args, **kwargs):
        cls._file_ = getmodule(cls).__file__

        @override_settings(TEST=True)
        def test_runner(self):
            js = str(Path(self._file_).with_suffix('.js'))
            url = str(self.live_server_url)
            run(['wdio', 'run', 'wdio.headless.conf.js', '--baseUrl', url, '--spec', js], check=True)

        setattr(cls, 'test_runner', test_runner)
