import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


#BASE DE DATOS POSTGRESQL
POSTGRESQL = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'db_tienda_online',

        'USER': 'postgres',

        'PASSWORD': 'dinero240901',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}