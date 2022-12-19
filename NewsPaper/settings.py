"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-7onuvmp&6ta@j9oeyr22m^mki3e((izh-_#r6ef&&oyoc@wmzk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
     #пользователей добавляют
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
     #сообщения добавляют
    'django.contrib.messages',

    'django.contrib.staticfiles',

    # Добавляем  для нашего приложения
    # 'news',
    'django.contrib.sites',   #настройки сайта
    'django.contrib.flatpages',
    'django_filters',

     # `allauth` обязательно нужен этот набор
     # В данный раздел добавьте 3 обязательных приложения allauth
     # и одно, которое отвечает за выход через Yandex
    'allauth',
    'allauth.account',
    'accounts.apps.AccountsConfig',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',

    # надо указать не имя нашего приложения, а его конфиг, чтобы всё заработало
    'appointments.apps.AppointmentsConfig',
    'news.apps.NewsConfig',
    # 'appointments',
    'django.core.mail',
    # 'django.contrib.sites',
    'django_apscheduler',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
     #добавляем
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' ,
    # добавляем для кеширования
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

# для `allauth` Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    #аутентификацию по username
    'django.contrib.auth.backends.ModelBackend',
    #бэкенд аутентификации
    'allauth.account.auth_backends.AuthenticationBackend',
]


ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # `allauth` обязательно нужен этот процессор
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

#используется в случае, если данный проект управляет несколькими сайтами
SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#После входа  в приложение нас перенаправит на страницу
LOGIN_REDIRECT_URL = "/news"



# для  различных способов регистрации/авторизации
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_USERNAME_REQUIRED = False
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_VERIFICATION = 'none'
#  добавили и изменили
ACCOUNT_EMAIL_VRIFICATION = 'mandatory'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTIFICATION_METHOD = 'email'


EMAIL_HOST = 'SMTP.yandex.ru'  # адрес сервера Яндекс-почты для всех один и тот же
EMAIL_PORT = 465  # порт smtp сервера тоже одинаковый
EMAIL_HOST_USER = 'magsy56'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'Magsy56!'  # пароль от почты
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно

ADMINS = [
    ('Gorik', 'vagren@mail.ru'),
    # список всех админов в формате ('имя', 'их почта')
]
MANAGERS = [
    ('Zina', 'vagren@mail.ru'),
    # список всех менеджеров в формате ('имя', 'их почта')
]

SERVER_EMAIL = 'magsy56@yandex.ru'  # это будет у нас вместо аргумента FROM в массовой рассылке

DEFAULT_FROM_EMAIL = 'magsy56@yandex.ru'
#DEFAULT_FROM_EMAIL = EMAIL_HOST_USER +  ‘@yandex.ru’

# формат даты, которую будет воспринимать наш задачник (вспоминаем модуль по фильтрам)
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"

# если задача не выполняется за 25 секунд, то она автоматически снимается, можете поставить время побольше, но как правило, это сильно бьёт по производительности сервера
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds

SITE_URL = 'http://127.0.0.1:8000'

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'TIMEOUT': 30,
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'), # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'FINFO': {
            'format': '%(asctime)s %(levelname)-8s %(module)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'FDEBUG': {
            'format': '%(asctime)s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'FWARNING': {
            'format': '%(asctime)s %(pathname)-12s %(levelname)-8s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'FERROR': {
            'format': '%(asctime)s %(pathname)-12s %(levelname)-8s %(message)s %(exc_info)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    #    'user_filter': {
    #        '()': 'news.views.UserFilter',
    #    },
    },
    'handlers': {
        'HDEBUG': {
            'class': 'logging.StreamHandler',
            'formatter': 'FDEBUG',
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            #'filters': ['user_filter'],
        },
        'HWARNING': {
            'class': 'logging.StreamHandler',
            'formatter': 'FWARNING',
            'level': 'WARNING',
            'filters': ['require_debug_true'],
        },
        'HERROR': {
            'class': 'logging.StreamHandler',
            'formatter': 'FERROR',
            'level': 'ERROR',
            'filters': ['require_debug_true'],
        },
        'HFILE': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR /'general.log',
            'formatter': 'FINFO',
        },
        'HFILE_ERROR': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR /'errors.log ',
            'formatter': 'FERROR',
        },
        'HFILE_SECURITY': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR /'security.log ',
            'formatter': 'FINFO',
        },
        'HMAIL': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'FWARNING',
            'filters': ['require_debug_false'],
        }
    },
    'root': {
        'handlers': ['HWARNING','HDEBUG'],
        'level': 'DEBUG',
        'propagate': True
    },
    'loggers': {
        'django': {
            'handlers': ['HERROR','HFILE'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['HFILE_ERROR', 'HMAIL'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['HFILE_ERROR', 'HMAIL'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['HFILE_ERROR'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['HFILE_ERROR'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['HFILE_SECURITY'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}


