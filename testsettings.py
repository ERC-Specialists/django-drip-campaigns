# MUST SPECIFY TO MAKE USE OF DJANGO DRIP
DRIP_FROM_EMAIL = ""
DEBUG = True

SECRET_KEY = "whatever/you/want-goes-here"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "sqlite.db",
    },
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.sessions",
    "django.contrib.contenttypes",
    "django.contrib.staticfiles",
    "django.contrib.messages",
    "django.contrib.sites",
    "drip",
    # testing only
    "credits",
)

MIDDLEWARE = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
            ],
        },
    },
]

AUTH_PROFILE_MODULE = "credits.Profile"

ROOT_URLCONF = "test_urls"

STATIC_URL = "/static/"
STATICFILES_DIRS = ()

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DRIP_CLASS_NAME = "drip.Drip"

# Default SCHEDULER to CELERY for testing purposes
DRIP_SCHEDULE_SETTINGS = {
    "DRIP_SCHEDULE": True,
    "DRIP_SCHEDULE_DAY_OF_WEEK": "*",
    "DRIP_SCHEDULE_HOUR": 12,
    "DRIP_SCHEDULE_MINUTE": 00,
    "SCHEDULER": "CELERY",
}

DRIP_UNSUBSCRIBE_USERS = True

SITE_ID = 1
