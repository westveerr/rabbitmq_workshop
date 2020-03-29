#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('136.144.135.215'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello Workshop Test!')
print(" [x] Hello Workshop Test!")

connection.close()
