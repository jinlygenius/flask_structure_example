import os
import datetime

# setting_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
setting_path = os.path.dirname(os.path.abspath(__file__))

BASE_DIR_LOG = os.path.join(os.path.sep, setting_path, 'logs')
# print(BASE_DIR_LOG)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'app': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': os.path.join(os.path.sep, BASE_DIR_LOG, 'app.log'),
            'mode': 'a',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
        },
        'user': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'verbose',
            'filename': os.path.join(os.path.sep, BASE_DIR_LOG, 'user.log'),
            'mode': 'a',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
        },
    },
    'formatters': {
        'verbose': {
            # 'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
            'format': '%(levelname)s %(asctime)s %(module)s %(funcName)s %(lineno)d %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'loggers': {
        'wsgi': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'app': {
            'handlers': ['console', 'app'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'user': {
            'handlers': ['console', 'user'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
