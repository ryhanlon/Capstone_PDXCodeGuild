from .settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'storia-dev-db',
        'USER': 'RebeccaHanlon',
        'PORT': 5432,
        'HOST': 'storia-dev-db.cigo70j0iacq.us-west-2.rds.amazonaws.com',
        'PASSWORD': os.environ['AWS_PASSWORD'],
    }
}

