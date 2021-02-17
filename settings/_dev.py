# used this file to change or specify settings while developing

# set debug mode for developing
DEBUG = True

# minimal secret key, do not use for production
SECRET_KEY = 'super-secret-key-change-me'

# set allowed hosts
ALLOWED_HOSTS = [
    'localhost',
]

# use sqlite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
