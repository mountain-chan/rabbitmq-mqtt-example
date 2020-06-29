import datetime

import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# for i in range(10000):
#     channel.basic_publish(exchange='logs', routing_key='', body="Log: " + str(i))
# connection.close()


while True:
    now_in_second = datetime.datetime.now().timestamp()
    channel.basic_publish(exchange='logs', routing_key='', body=str(now_in_second))
    print("Sent log: " + str(now_in_second))
    # time.sleep(1)



