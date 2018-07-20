import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(
    exchange='direct_logs',
    exchange_type='direct'
)

channel.basic_publish(
    exchange='direct_logs',
    routing_key='Critical',
    body='Something critical happened!'
)

print('message sent')
connection.close()