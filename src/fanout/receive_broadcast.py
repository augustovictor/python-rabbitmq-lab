import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

result = channel.queue_declare(exclusive=True)

QUEUE_NAME = result.method.queue

channel.queue_bind(exchange='logs', queue=QUEUE_NAME)

def callback(ch, method, properties, body):
    print(f'Received message: {body}')

channel.basic_consume(callback, queue=QUEUE_NAME, no_ack=True)

channel.start_consuming()