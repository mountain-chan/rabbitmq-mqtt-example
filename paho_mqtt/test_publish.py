import timeit

setup = """
import paho.paho_mqtt.client as paho_mqtt

broker_address = "localhost"
client = paho_mqtt.Client(client_id="client_publish")
client.connect(broker_address)
client.loop_start()
"""

ex1 = """ 
for i in range(100000):
    client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
client.disconnect()
"""

long = timeit.timeit(ex1, setup=setup, number=1)
print(long)
