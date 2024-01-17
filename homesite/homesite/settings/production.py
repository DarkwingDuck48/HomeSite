"""TODO: Add POSTGRES database
"""

from homesite.settings.common import *
import os

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'production.sqlite3',
    }
}