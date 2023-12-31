import os
from decouple import config
import dj_database_url


DEBUG = True

USE_TZ = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

USE_I18N = True

USE_L10N = True

DATABASES = {
	'default': dj_database_url.parse(config('DATABASE_URL'))
}
    #  {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': config('NAME'), 
    #     'USER': config('USER'), 
    #     'PASSWORD': config('PASSWORD'),
    #     'HOST': '127.0.0.1', 
    #     'PORT': '5432',
	# }
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
			]
		}
	}
]

TIME_ZONE = 'UTC'

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
 	"whitenoise.middleware.WhiteNoiseMiddleware",
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECRET_KEY = config('SECRET_KEY')

STATIC_URL = '/static/'

# STATICFILES_STORAGE  = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

ROOT_URLCONF = 'my_portfolio.urls'

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'en-us'

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'corsheaders',
	'rest_framework',
	'portfolio',
]

WSGI_APPLICATION = 'my_portfolio.wsgi.application'

CORS_ALLOW_HEADERS = [
	'x-requested-with',
	'content-type',
	'accept',
	'origin',
	'authorization',
	'accept-encoding',
	'x-csrftoken',
	'access-control-allow-origin',
	'content-disposition',
]

CORS_ALLOW_METHODS = [
	'GET',
	'POST',
	'PUT',
	'PATCH',
	'DELETE',
	'OPTIONS',
]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True

AUTH_PASSWORD_VALIDATORS = [
	{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
	{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
	{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
	{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


CLOUDINARY_STORAGE = {
	'API_KEY': config('API_KEY'),
	'API_SECRET': config('API_SECRET'),
	'CLOUD_NAME': config('CLOUD_NAME'),
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
