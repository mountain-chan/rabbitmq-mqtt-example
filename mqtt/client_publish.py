import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log " + buf)


broker_address = "localhost"
# broker_address = "test.mosquitto.org"

client = mqtt.Client(client_id="client_publish")
# client.on_log = on_log
client.connect(broker_address)  # connect to broker
client.loop_start()

i = 1
while True:
    client.publish(topic="my/topic", payload="Message: " + str(i), qos=1, retain=True)
    print("send message: " + str(i))
    i += 1
    time.sleep(2)
