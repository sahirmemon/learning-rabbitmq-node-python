#!/usr/bin/env python
import pika

# Create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))

# Create a channel
channel = connection.channel()

# Connect to the queue 'hello'
channel.queue_declare(queue='hello')

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)

# Tell RabbitME that this particular callback function should receive message from
# our hello queue
channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
