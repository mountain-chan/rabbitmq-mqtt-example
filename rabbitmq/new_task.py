import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Task ....: "
i = 1
while True:
    channel.basic_publish(
        exchange='',
        routing_key='task_queue',
        body=message+str(i),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(" [x] Sent %r" % message+str(i))
    i += 1
    time.sleep(2)

# connection.close()
