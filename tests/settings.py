DEBUG = True
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
	}
}
TEMPLATES = [{
	'BACKEND': 'django.template.backends.django.DjangoTemplates',
	'APP_DIRS': True,
	'OPTIONS': {
		'context_processors': [
			'django.contrib.auth.context_processors.auth',
			'django.contrib.messages.context_processors.messages',
		]
	},
	'DIRS': []
}]

MIDDLEWARE = ()
# Required for Django 1.4+
STATIC_URL = '/static/'

# Required for Django 1.5+
SECRET_KEY = 'abc123'
