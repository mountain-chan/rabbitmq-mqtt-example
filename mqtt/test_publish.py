import timeit

setup = """
import paho.mqtt.client as mqtt

broker_address = "localhost"
client = mqtt.Client(client_id="client_publish")
client.connect(broker_address)
client.loop_start()
"""

ex1 = """ 
for i in range(10000):
    client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
client.disconnect()
"""

long = timeit.timeit(ex1, setup=setup, number=1)
print(long)
