import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"

i = 1
while True:
    channel.basic_publish(exchange='logs', routing_key='logs', body=message + str(i))
    print(" [x] Sent %r" % message + str(i))
    i += 1
    time.sleep(3)

# connection.close()

