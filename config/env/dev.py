from config.settings import *  # noqa: F403

DEBUG = True

# allauth
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_VERIFICATION_BY_CODE_ENABLED = False

HEADLESS_SERVE_SPECIFICATION = True
HEADLESS_SPECIFICATION_TEMPLATE_NAME = 'headless/spec/swagger_cdn.html'
SPECTACULAR_SETTINGS = {
    'EXTERNAL_DOCS': {'description': 'allauth', 'url': '/_auth/openapi.html'},
}


# database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # noqa: F405
    }
}
