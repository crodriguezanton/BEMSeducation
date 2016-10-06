from BEMSeducation.common_settings import *
from BEMSauth.private_settings import *

""" Static files and media (CSS, JavaScript, Images) """
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
ENV_PATH = os.path.abspath(os.path.dirname(__file__))
MEDIA_ROOT = os.path.join(ENV_PATH, '../static_server/media/')
STATIC_ROOT = os.path.join(ENV_PATH, '../static_server/static/')

# This one is just useful during development, on production statics and media should be served by nginx / apache
MEDIA_URL = '/media/'
STATIC_URL = '/static/'

DEBUG = False
ALLOWED_HOSTS = ['.bems.cat']