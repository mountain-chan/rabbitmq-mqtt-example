import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log " + buf)


broker_address = "localhost"
# broker_address = "test.mosquitto.org"

client = mqtt.Client("client_publish")
# client.on_log = on_log
client.connect(broker_address)  # connect to broker

i = 1
while True:
    client.publish("my/topic", "Message: " + str(i))
    print("send message: " + str(i))
    i += 1
    time.sleep(3)
