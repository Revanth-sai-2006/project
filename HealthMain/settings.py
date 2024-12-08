from pathlib import Path

# Base directory path
BASE_DIR = Path(__file__).resolve().parent.parent

# Security key
SECRET_KEY = 'django-insecure-xxxxxxxxxxxxxxxxxxxx'

# Debug mode
DEBUG = True

# Allowed hosts for the application
ALLOWED_HOSTS = ['*']  # You can restrict this to specific hosts later in production

# Installed applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminapp',  # Add your apps here
    'staffapp',
    'patientapp',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF middleware
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration
ROOT_URLCONF = 'HealthMain.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Path to templates directory
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

# WSGI application
WSGI_APPLICATION = 'HealthMain.wsgi.application'

# Database configuration (using SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Language and timezone settings
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'

# Static files (CSS, JavaScript, images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Path to static files directory
]

# CSRF settings (newly added)
CSRF_TRUSTED_ORIGINS = ['http://localhost:8000']  # Add the domain/port you're working with
CSRF_COOKIE_HTTPONLY = False  # Ensure frontend can access the CSRF token for POST requests

# settings.py



# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'venkatanagabalaji124@gmail.com'
EMAIL_HOST_PASSWORD = 'npcv nusb rizz vudg'
DEFAULT_FROM_EMAIL = 'venkatanagabalaji124@gmail.com'

# settings.py
TWILIO_ACCOUNT_SID = 'AC3990c71de3e5f3840c3bb33f511acfab'
TWILIO_AUTH_TOKEN = 'bf54493583eae83a5e6b8c26a32931ce'
TWILIO_PHONE_NUMBER = '+17752966522'