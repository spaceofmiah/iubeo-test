from iubeo import config, comma_separated_list, boolean


# def list_from_string(val):
#     return val.split(',')


CONFIG = config({
    'DATABASE': {
        'USER': str,
        'PASSWORD': str,
        'HOST': str,
        'PORT': str,
        'NAME': str,
    },
    'DEBUG': boolean,
    'SECRET_KEY': str,
    'ALLOWED_HOSTS': comma_separated_list,
})
