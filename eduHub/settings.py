
import os
import django_heroku
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%_2x5(!4-gk%m4$4-m!&88y-d#d7_d9@)$dl7uqdzf%dd+u3q1'
# SECRET_KEY = os.getenv('SECRET_KEY')   #for production
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',  # remove for production
    'user',
    'home',
    'material',
    'channels',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # remove for production
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eduHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'eduHub.wsgi.application'
ASGI_APPLICATION = "eduHub.routing.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# Production database settings
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'eduHub',
#     }
# }

# Default sqllite database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/create-test/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/instructor-portal/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/student-test/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/check-test/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/instructor-portal-test/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/create-test-series/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/instructor-portal-testSeries/build/static/"),
    os.path.join(
        BASE_DIR, "material/templates/material/test-result/build/static/"),
]
# serving static files in development  Put all static files to azure container for production
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# for local dev server
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# for production
# DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
# MEDIA_URL = 'https://eduhub.blob.core.windows.net/eduhub/'
# AZURE_CONTAINER = "eduhub"
# AZURE_CONNECTION_STRING = os.getenv('AZURE_CONNECTION_STRING')

# CORS settings for development remove for production
CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


LOGIN_URL = '/user/login/'
LOGOUT_REDIRECT_URL = '/'

django_heroku.settings(locals())
