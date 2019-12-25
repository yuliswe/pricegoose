from django.conf import settings


def run(*args):
    settings.MIGRATION_MODULES_ROOT.mkdir(exist_ok=True)
    (settings.MIGRATION_MODULES_ROOT / '__init__.py').touch(exist_ok=True)

    for app in settings.DROPPIE_APPS:
        (settings.MIGRATION_MODULES_ROOT / app).mkdir(exist_ok=True)
        (settings.MIGRATION_MODULES_ROOT / app / '__init__.py').touch(exist_ok=True)
