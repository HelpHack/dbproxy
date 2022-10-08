import os
from mongoengine import *
from logger import Logger

def connect_to_db():
    dbname = os.environ.get('DB_NAME', 'oxylion')
    host = os.environ.get('DB_HOST', 'localhost')
    port = os.environ.get('DB_PORT', '27017')
    username = os.environ.get('DB_USERNAME', '')
    password = os.environ.get('DB_PASSWORD', '')
    credentials = '' if len(username) == 0 else f'{username}:{password}@'
    uri = ['mongodb://', credentials, host, ':', port, '/', dbname]
    try:
        connect(
            'oxylion',
            host=''.join(uri)
        )
        Logger.debug('Connected to database')
    except ConnectionFailure as e:
        Logger.error('Could not connect to database: {}'.format(e))