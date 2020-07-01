import datetime
import time
from urllib.parse import urlparse

import paho.mqtt.client as mqtt

broker_address = "mqtt://bootai:1234567aA@@localhost:1883"
broker_url = urlparse(broker_address)
client = mqtt.Client()
client.username_pw_set(username=broker_url.username, password=broker_url.password)
client.connect(broker_url.hostname, broker_url.port)
client.loop_start()

# for i in range(10000):
#     client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
# client.disconnect()

while True:
    now_in_second = datetime.datetime.now().timestamp()
    client.publish(topic="my/topic", payload=now_in_second, retain=True)
    print("Sent message: " + str(now_in_second))
    # time.sleep(1)
