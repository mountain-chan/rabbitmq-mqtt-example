import timeit

setup = """
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.exchange_declare(exchange='logs', exchange_type='fanout')
"""

ex1 = """
for i in range(10000):
    channel.basic_publish(exchange='logs', routing_key='', body="Log: " + str(i))
connection.close()
"""

long = timeit.timeit(ex1, setup=setup, number=1)
print(long)
