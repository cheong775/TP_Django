"""
Django settings for TP_Django project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0+exb_)jr8dxyafhg5#^ts@-l*lf(lj-mjqzlol65!jsro3=f^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #这里是指是否开启debug测试模式，如果不想开启就把它改成False关闭在生长环境下建议关闭

ALLOWED_HOSTS = [] #当debug模式开启时允许监听的地址访问的主机把他们的地址写进去


# Application definition
#↓我们创建的应用app要添加到这里面去
INSTALLED_APPS = [
    'django.contrib.admin',#管理站点
    'django.contrib.auth', #权限认证框架
    'django.contrib.contenttypes',#内容类型框架
    'django.contrib.sessions',#会话框架
    'django.contrib.messages',#消息框架
    'django.contrib.staticfiles',#管理静态文件的框架
    'todo'
]
#↓中间键不需要改
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#↓根路由配置文件
ROOT_URLCONF = 'TP_Django.urls'

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

WSGI_APPLICATION = 'TP_Django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
#↓包含了所有的项目所使用的数据库默认使用sqlite3，如果要使用mysql就要把这里改掉
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'  #文字编码

TIME_ZONE = 'UTC'

USE_I18N = True  #GUI源码 

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'  #静态文件路径