import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = 'Fanout message'

channel.basic_publish(exchange='logs', routing_key='', body=message)

print('Message sent')
connection.close()