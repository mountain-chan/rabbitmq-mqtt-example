import datetime
import time

import paho.mqtt.client as mqtt

broker_address = "localhost"
client = mqtt.Client(client_id="client_publish")
client.connect(broker_address)
client.loop_start()

# for i in range(10000):
#     client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
# client.disconnect()

i = 0
while True:
    now_in_second = datetime.datetime.now().timestamp()
    client.publish(topic="my/topic", payload=now_in_second, retain=True)
    print("Sent message: " + str(now_in_second))
    i += 1
    # time.sleep(1)
