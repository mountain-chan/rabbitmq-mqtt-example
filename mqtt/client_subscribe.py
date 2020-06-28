import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    client.subscribe(topic="my/topic")


def on_message(client, userdata, message):
    print(message.payload)


broker_address = "localhost"
# broker_address = "iot.eclipse.org"
# broker_address = "test.mosquitto.org"

client = mqtt.Client(client_id="client_subscribe")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address)  # connect to broker

client.loop_forever()
client.disconnect()
