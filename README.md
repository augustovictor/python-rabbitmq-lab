# python-rabbitmq-lab

Running RabbitMQ with docker:
`docker pull rabbitmq:3-management-alpine`

`docker run --name rabbit-with-management -p 5672:5672 -p 15672:15672 rabbitmq:3-management-alpine`

`5672`: Port to connect to rabbimq
`15672`: Port to management. `localhost:15672`. username and password: `guest`

## Publisher confirms

## Message TTL