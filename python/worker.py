#!/usr/bin/env python
import pika
import time

# Create connection
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))

# Create a channel
channel = connection.channel()

# Connect to the queue 'hello'
channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print (" [x] Received %r" % body)
    time.sleep( body.count(b'.') )
    print (" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)


# Tell RabbitME that this particular callback function should receive message from
# our hello queue
channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue='hello')

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
