import mongoengine
import routes
import schemas
import connect
import mq

if __name__ == '__main__':
    connect.connect_to_db()
    mq.MQ()