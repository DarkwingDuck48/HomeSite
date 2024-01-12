"""TODO: Add POSTGRES database
"""

from homesite.settings.common import *
import os

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']