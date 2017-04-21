# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'Sample key, replace with secure key in production!'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hit_hit_crit',
        'USER': 'db user',
        'PASSWORD': 'db password',
        'HOST': 'db host',
        'PORT': 'db port',
    }
}

MEDIA_ROOT = '/var/www/hithitcrit.co.uk/media/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False 
