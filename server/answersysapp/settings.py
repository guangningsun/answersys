import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'y8)ahmo4#n)aoatj@en2r#f_u99l&b)%9z22+r--j7(+aq)w57'
DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'simpleui',
    'rest_framework',
    'django_filters',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'answersysapp',
    'AppModel',
    'corsheaders',
    'mptt',
    'django_extensions',
    'werkzeug_debugger_runserver',
]

# env need pip install django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

ROOT_URLCONF = 'answersysapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates'],
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

WSGI_APPLICATION = 'answersysapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'OPTIONS': {
            'timeout': 30,
        }
    }

}

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

LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

# simple ui setting
# ????????????????????????
SIMPLEUI_HOME_INFO = False
# ??????????????????
SIMPLEUI_HOME_ACTION = True
# ????????????????????????
SIMPLEUI_ANALYSIS = False
# ??????????????????
IMPORT_EXPORT_USE_TRANSACTIONS = True
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


SIMPLEUI_CONFIG = {
    'menus': [{
        'app': 'AppModel',
        'name': '??????????????????',
        'icon': 'fab fa-dashcube',
        'models': [{
            'name': '????????????',
            'url': 'AppModel/companyinfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/userinfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/awardinfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/questionbank',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/testpaperinfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/examscore',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/actioninfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/useraward',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/prizeinfo',
            'icon': 'fa fa-server'
        },{
            'name': '????????????',
            'url': 'AppModel/userprizeinfo',
            'icon': 'fa fa-server'
        }]
        },{
        'app': 'auth',
        'name': '????????????',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '????????????',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },{
            'name': '?????????',
            'icon': 'fa fa-users',
            'url': 'auth/group/'
        }]
    }]
}

MPTT_ADMIN_LEVEL_INDENT = 20
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
PRCODE_ROOT = os.path.join(BASE_DIR, 'prcode')
PRCODE_URL = '/prcode/'
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#CSRF_TRUSTED_ORIGINS = ['brilliantlife.com.cn']
#CSRF_TRUSTED_ORIGINS = ['*']
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'http')
CONF_DIR = os.path.join(BASE_DIR, "conf/answersys.conf")