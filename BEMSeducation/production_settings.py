from BEMSeducation.common_settings import *
from BEMSauth.private_settings import *

""" Static files and media (CSS, JavaScript, Images) """
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(BASE_DIR, '../static_server/media/')
STATIC_ROOT = os.path.join(BASE_DIR, '../static_server/static/')

# This one is just useful during development, on production statics and media should be served by nginx / apache
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEBUG = True
ALLOWED_HOSTS = ['.bems.cat']

SESSION_COOKIE_DOMAIN = '.bems.cat'

SOCIALACCOUNT_PROVIDERS = \
    { 'google':
        { 'SCOPE': ['profile', 'email'],
          'AUTH_PARAMS': { 'access_type': 'online' } }}

SOCIALACCOUNT_QUERY_EMAIL = True

LOGIN_URL = 'http://secure.bems.cat/login/'

RAVEN_CONFIG = {
    'dsn': 'https://80379e3334ac409290319ae4f7f20929:db8d47a4fd1245549ca770978408d721@sentry.io/103682',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/BEMS/debug.log',
        }
    },
    'loggers': {
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['file'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['file'],
            'propagate': False,
        },
    },
}