import re
from os import environ
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
      
# Token Verification Info :
VERIFY = bool(environ.get('VERIFY', True))
VERIFY_SECOND_SHORTNER = bool(environ.get('VERIFY_SECOND_SHORTNER', False))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', 'modijiurl.com')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '7428b77c62b287c0c7c8b8dc62eedaa8b5bf7246')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://youtu.be/r-jOcfquYsY?si=kP8kKSjoojovFGS9')

# if verify second shortner is True then fill below url and api
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', 'https://youtu.be/r-jOcfquYsY?si=kP8kKSjoojovFGS9')

# Shortlink Info
SHORTLINK_MODE = bool(environ.get('SHORTLINK_MODE', True))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'modijiurl.com')
SHORTLINK_API = environ.get('SHORTLINK_API', '7428b77c62b287c0c7c8b8dc62eedaa8b5bf7246')
