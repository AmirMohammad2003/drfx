from .base import *


ALLOWED_HOSTS += ['localhost']

# WSGI_APPLICATION = 'home.wsgi.dev.application'

CORS_ORIGIN_WHITELIST = (
    # dev server for react.js
    'http://localhost:3000',
)
