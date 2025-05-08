from config.settings import *  # noqa: F403
from config.settings import BASE_DIR

DEBUG = False

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

STATIC_ROOT = BASE_DIR / 'staticfiles'
