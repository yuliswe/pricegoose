import subprocess
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

    def __init_subclass__(subcls, *args, **kwargs):  # noqa
        subcls._file_ = getmodule(subcls).__file__

        @override_settings(TEST=True)
        def test_runner(self):
            js = str(Path(self._file_).with_suffix('.js'))
            url = str(self.live_server_url)
            subprocess.run(
                ['wdio', 'run', 'wdio.headless.conf.js', '--baseUrl', url, '--spec', js],
                cwd=Path(__file__).parent,
                check=True
            )

        setattr(subcls, 'test_runner', test_runner)
