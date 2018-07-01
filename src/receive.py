import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
QUEUE_NAME = 'task_queue'
channel.queue_declare(queue=QUEUE_NAME, durable=True)

def callback(ch, method, properties, body):
    print(f'Message received: {body}')
    time.sleep(body.count(b'.'))
    ch.basic_ack(delivery_tag = method.delivery_tag)
    print('Done!')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue=QUEUE_NAME)

print('Listening for messages...')

channel.start_consuming()