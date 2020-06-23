import time

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

i = 1
while True:
    channel.basic_publish(exchange='', routing_key='hello', body='Hello World!'+str(i))
    print(" [x] Sent 'Hello World!'"+str(i))
    i += 1
    time.sleep(3)


# connection.close()
