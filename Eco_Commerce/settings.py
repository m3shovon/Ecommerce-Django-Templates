

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = Path.joinpath(BASE_DIR , 'templates')
STATIC_DIR = Path.joinpath(BASE_DIR , 'static')
MEDIA_DIR = Path.joinpath(BASE_DIR , 'media')



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ve$r9!fwa&$kk@yo-%06()pu@v*#3m-=bvdv&)y^@ida*ad35z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin', 
    'admin_interface', 
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'crispy_forms', 'crispy_bootstrap4', 
    'App_Login', 'App_Shop', 'App_Order', 'App_Payment', 'App_Settings', # 'App_UserLog', 
    'django_check_seo', 'cms', 'menus', 'treebeard'

]

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

# Use django-admin-interface package
ADMIN_INTERFACE_SETTING = {
    'theme': 'default',  # choose a theme
    'favicon': '/static/favicon.ico',  # path to your favicon
    'navigation': 'vertical',  # or 'horizontal'
    'list_filter_dropdown': False,  # enable/disable dropdown for list filter
    'search_placeholder': 'Search here...',  # placeholder for search bar
    'show_sidebar': True,  # enable/disable sidebar
    'show_title': True,  # enable/disable title
    'show_breadcrumbs': True,  # enable/disable breadcrumbs
    'show_topnav': True,  # enable/disable top navigation
}

SITE_ID = 1


CRISPY_TEMPLATE_PACK = 'bootstrap4'

# custom user model:
AUTH_USER_MODEL = 'App_Login.User'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Eco_Commerce.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR,],
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

WSGI_APPLICATION = 'Eco_Commerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'e-commerce',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'USER': 'root',
#         'PASSWORD': '',
#     }
# }


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

TIME_ZONE = 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = 'media/'

LOGIN_URL = '/account/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# THEME = 'bootstrap'

# 'default'
# 'flat'
# 'material'
# 'bootstrap'
# 'foundation'
# 'adminlte'
# 'metro