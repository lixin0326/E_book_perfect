import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
sys.path.insert(1, os.path.join(BASE_DIR, "ext_apps"))

SECRET_KEY = 'dn&etnz41-18l#i*)67a$1s1^d+*pov63%o4)!5adjub=elq7k'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

]

# 业务扩展应用注册表
INSTALLED_MYAPPS = [
    # 首页
    'apps.home',
    # 详情页面
    'apps.detail',
    # 购物车页面
    'apps.car',
    # 搜索页面
    'apps.search',
    # 　后台管理　
    'xadmin',
    'crispy_forms',
    # 用户评论
    'apps.comments',

    # 登录注册板块
    'apps.account',
    # 订单
    'apps.order',
    # 支付功能模块
    'apps.pay',

    'apps.drf_apis',
    'rest_framework',
    # 富文本
    'djcelery',

    'DjangoUeditor',
]

INSTALLED_APPS += INSTALLED_MYAPPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wh1804_bookstore.urls'

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
                'apps.account.context_processors.shop_count',  # 注册全局变量
            ],
        },
    },
]

WSGI_APPLICATION = 'wh1804_bookstore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_bookstore',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '1234',
        'CHARSET': 'utf8'
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

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_ROOT = os.path.join(BASE_DIR, "static")

from django.contrib.messages import constants as message_constants

MESSAGE_LEVEL = message_constants.INFO

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

SEX_CHOICES = [
    ('M', '男人'),
    ('F', '女人'),
]

USER_CHOICES = [
    (0, '普通会员'),
    (1, 'VIP会员'),
    (2, '黄金会员'),
]

DINNER_CHOICES = [
    (0, '待下单'),
    (1, '已下单')
]

PAY_CHOICES = [
    (0, '货到付款'),
    (1, '微信支付'),
    (2, '支付宝支付'),
]

DB_FIELD_VALID_CHOICES = [
    (0, '未删除'),
    (1, '已删除'),
]

#########################Django Logging  BEGIN######################

# LOGGING_DIR 日志文件存放目录
LOGGING_DIR = "./logs"
if not os.path.exists(LOGGING_DIR):
    os.mkdir(LOGGING_DIR)

import logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s][%(funcName)s][%(lineno)d] > %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s]> %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': '%s/django.log' % LOGGING_DIR,
            'formatter': 'standard'
        },  # 用于文件输出
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'mdjango': {
            'handlers': ['console', 'file_handler'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}


# logger = logging.getLogger("mdjango")


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonLogger(Singleton):
    def __init__(self):
        super(SingletonLogger, self).__init__()
        self.__logger = logging.getLogger("mdjango")

    def slogger(self):
        return self.__logger


sinlogger = SingletonLogger().slogger()

########################## Django Logging  END#########################

################# E_mail settings begin #################

EMAIL_HOST = 'smtp.163.com'

EMAIL_PORT = 465
EMAIL_USE_SSL = True
# EMAIL_USE_TLS = False
# 此账号是测试账号，不要乱用
EMAIL_HOST_USER = "L15737628530@163.com"

# 邮箱的客户端授权密码
EMAIL_HOST_PASSWORD = "lixin123"

################# E_mail settings end ###################

# =========支付宝配置相关=========
APP_ID = '2016092000556153'
# 上线支付
# ALI_PAY_URL = 'https://openapi.alipaydev.com/gateway.do'

# 测试支付环境
ALI_PAY_DEV_URL = 'https://openapi.alipaydev.com/gateway.do'

# 设置自己的私钥
APP_PRIVATE_KEY_PATH = os.path.join(BASE_DIR, 'key/app_private_key.pem')

# 支付宝的公钥
ALIPAY_PUBLIC_KEY_PATH = os.path.join(BASE_DIR, 'key/alipay_public_key.pem')

#######################支付宝end##############################

############### celery settings begin #############
'''
celery是分布式异步消息队列处理框架
以redis作为MQ数据存储和转发

注意:需要开启redis服务!!!!!!!!!!!!!!!!!!
'''
REDIS_DEPLOY_FLAG = "test"

REDIS_SERVICE = {
    'test': ('127.0.0.1', '6379'),
    'online': ('192.168.11.11', '10379'),
}

CELERY_BROKER_URL = 'redis://%s:%s/1' % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                         REDIS_SERVICE[REDIS_DEPLOY_FLAG][1])

CELERY_ACCEPT_CONTENT = ['json']

CELERY_TASK_SERIALIZER = 'json'

# CELERY_RESULT_BACKEND = 'django-db'

CELERY_RESULT_BACKEND = 'redis://%s:%s/2' % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                             REDIS_SERVICE[REDIS_DEPLOY_FLAG][1])

# 部署的django服务的IP和端口
DJANGO_SERVICE = ('127.0.0.1', 8688)

import redis

R = redis.Redis(host='127.0.0.1', port=6379, db=0)

CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://%s:%s/1" % (REDIS_SERVICE[REDIS_DEPLOY_FLAG][0],
                                         REDIS_SERVICE[REDIS_DEPLOY_FLAG][1]),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

############### celery settings end #############
