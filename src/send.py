import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
QUEUE_NAME = 'task_queue'
MAKE_MESSAGE_PERSISTENT = 2
channel.queue_declare(queue=QUEUE_NAME, durable=True)

message = ' '.join(sys.argv[1:]) or 'Hello world'
channel.basic_publish(
    exchange='',
    routing_key=QUEUE_NAME,
    body=message,
    properties=pika.BasicProperties(delivery_mode=MAKE_MESSAGE_PERSISTENT)
)

print('Message sent!')

connection.close()