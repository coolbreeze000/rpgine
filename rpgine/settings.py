"""
Django settings for rpgine project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

# import django mongodb drivers
# import mongoengine

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# TODO replace SECRET_KEY
# THIS KEY SHOULD ONLY BE USED FOR TESTING PURPOSES!!! THIS KEY WILL SHOULD BE REPLACES IN PRODUCTION ENVIRONMENTS!!!

SECRET_KEY = '6^+ajhhl64h8=g*55$mt5(t$g84om1u(egwd2uprgflp%@w$er'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'rpgine_core',
    'rpgine_comapp_danceofdragons',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

#'django.middleware.cache.UpdateCacheMiddleware',    # This must be first on the list
#'django.middleware.cache.FetchFromCacheMiddleware', # This must be last

ROOT_URLCONF = 'rpgine.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'string_if_invalid': 'INVALID EXPRESSION: %s',
        },
    },
]

WSGI_APPLICATION = 'rpgine.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# http://staltz.com/djangoconfi-mongoengine/#/15

# TODO uncomment to enable mongodb in general

"""
DATABASES = {
    'default': {
        'ENGINE': '',
    }
}
"""

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy',
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# TODO uncomment to enable mongodb session backend --> should later be moved to redis
#SESSION_ENGINE = 'mongoengine.django.sessions' # optional
#SESSION_ENGINE = 'django.contrib.sessions.backends.cache' # optional

"""
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': '192.168.99.100:6379',
        'OPTIONS': {
            'DB': 1,
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'PICKLE_VERSION': -1,
        },
    },
}

#            'PASSWORD': 'yadayada',
"""

# TODO uncomment to implement django integration with mongodb
"""
MONGODB_USER = 'admin'
MONGODB_PASSWD = 'admin'
MONGODB_HOST = '192.168.99.100' #boot2docker
MONGODB_NAME = 'rpgine'
MONGODB_DATABASE_HOST = 'mongodb://%s:%s@%s/%s' % (MONGODB_USER, MONGODB_PASSWD, MONGODB_HOST, MONGODB_NAME)

mongoengine.connect(MONGODB_NAME, host=MONGODB_DATABASE_HOST)

AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)
"""

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_ROOT = BASE_DIR
STATICFILES_DIRS = (
   STATIC_ROOT + '/static/',
)
STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = '/dashboard/'