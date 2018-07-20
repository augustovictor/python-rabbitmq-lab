import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)

severities = ['Critical', 'Debbug', 'Warning']

result = channel.queue_declare(exclusive=True)

queue_name = result.method.queue

for s in severities:
    channel.queue_bind(
        exchange='direct_logs',
        queue=queue_name,
        routing_key=s
    )

def callback(ch, method, properties, body):
    print(f'[x] {method.routing_key}: {body}')

channel.basic_consume(callback, queue=queue_name, no_ack=True)

print('Waiting for messages...')
channel.start_consuming()