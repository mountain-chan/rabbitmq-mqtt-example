import timeit

setup = """
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
"""

ex1 = """
for i in range(100000):
    channel.basic_publish(exchange='', routing_key='hello', body='Message: '+str(i))
connection.close()
"""

long = timeit.timeit(ex1, setup=setup, number=1)
print(long)

