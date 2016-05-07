from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = BASE_DIR + '/static/'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1i$kri-fg=*q$^8x)%+k58@p9s_9(tggmg1ge(s(g_2@r)sxf-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'testapp',
    'crispy_forms',
    'tastypie'
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

ROOT_URLCONF = 'Bitnomix.urls'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
SUIT_CONFIG = {
    'ADMIN_NAME': 'NeeleshBatham',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SEARCH_URL': '',
    'MENU_EXCLUDE': ('auth.group', 'auth', 'sites'),
    'MENU_OPEN_FIRST_CHILD': True,
    'LIST_PER_PAGE': 20,
    'SHOW_REQUIRED_ASTERISK': True,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/', BASE_DIR +'/article/templates/' ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.media",
                "django.core.context_processors.static",
            ],
        },
    },
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SUIT_CONFIG = {
#     'PARAM': VALUE,
#     'PARAM2': VALUE2
}


    # Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR + '/media/'


STATIC_ROOT = BASE_DIR + '/static/'+ 'static_root'

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),
)
