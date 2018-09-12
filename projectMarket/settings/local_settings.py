# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'marketfiyatim',
        'USER': 'marketfiyatim',
        'PASSWORD': 'marketfiyatim123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


SOCIAL_AUTH_TWITTER_KEY = 'qmi0KPcQSmUFfEwBSLb495m7L'
SOCIAL_AUTH_TWITTER_SECRET = 'w4zGBFyaqArRZRJ2bbfEmHXvuSm3P5HOzzWdSyZpze438D0rsV'


SOCIAL_AUTH_FACEBOOK_KEY = '2277086349235314'
SOCIAL_AUTH_FACEBOOK_SECRET = '1b65d140f4c1374e5e1d82ab9ff08891'