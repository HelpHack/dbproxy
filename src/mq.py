import pika
import os

from logger import Logger
from request_handler import handle_request

class MQ:
    # Create a global channel variable to hold our channel object in
    channel = None
    queue_receive = 'db-requests'
    queue_give = None

    # Get the connection string from the environment variable
    def get_url(self):
        user = os.environ.get('RABBITMQ_USER', 'guest')
        password = os.environ.get('RABBITMQ_PASS', 'guest')
        url = os.environ.get('RABBITMQ_URL', 'localhost')
        return f'amqp://{user}:{password}@{url}/' if len(url) else None

    def __init__(self):
        # Connect to the RabbitMQ server
        url = self.get_url()
        try:
            if url:
                connection = pika.BlockingConnection(pika.URLParameters(url))
            else:
                connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        except:
            Logger.error('RabbitMQ connection failed')
            return
        channel = connection.channel()
        # Create a queue
        channel.queue_declare(queue=self.queue_receive)
        self.queue_give = os.environ.get('RABBITMQ_REPLY_TO_QUEUE', None)
        if self.queue_give:
            channel.queue_declare(queue=self.queue_give)
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=self.queue_receive, on_message_callback=self.handle_delivery)
        Logger.debug('Waiting for messages...')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
            connection.close()
            Logger.debug('Connection closed')
            print('bye...')

    def handle_delivery(self, channel, method, properties, body):
        Logger.debug('Received message')
        result = handle_request(body)
        if properties.reply_to:
            channel.basic_publish(exchange='', routing_key=properties.reply_to, body=result)
        else:
            if self.queue_give:
                channel.basic_publish(exchange='', routing_key=self.queue_give, body=result)
            else:
                Logger.error('No reply_to property. Please specify reply_to=\'amq.rabbitmq.reply-to\'')
        channel.basic_ack(delivery_tag=method.delivery_tag)
