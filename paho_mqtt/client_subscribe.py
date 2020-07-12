import datetime
from urllib.parse import urlparse

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic="my/topic")


def on_message(client, userdata, message):
    time_send = float(message.payload.decode("utf-8"))
    now_in_second = datetime.datetime.now().timestamp()
    print(now_in_second-time_send)


broker_address = "paho_mqtt://bootai:1234567aA@@localhost:1883"
broker_url = urlparse(broker_address)
client = mqtt.Client()
client.username_pw_set(username=broker_url.username, password=broker_url.password)
client.connect(broker_url.hostname, broker_url.port)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
client.disconnect()
