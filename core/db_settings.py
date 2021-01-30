from core.config import CONFIG

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": CONFIG.DATABASE.NAME,
        "USER": CONFIG.DATABASE.USER,
        "PASSWORD": CONFIG.DATABASE.PASSWORD,
        "HOST": CONFIG.DATABASE.HOST,
        "PORT": CONFIG.DATABASE.PORT,
    }
}
