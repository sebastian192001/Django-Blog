from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['djangoblog19.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dolkv78kmnevp',
        'USER': 'ozhjybuqciists',
        'PASSWORD': '3143155eadb18d4a3ce5ec22da7df4646d91908725c3c44d811356fb967eb57e',
        'HOST': 'ec2-23-20-70-32.compute-1.amazonaws.com',
        'PORT': 5432,

    }
}



STATICFILES_DIRS = (BASE_DIR, 'static')
