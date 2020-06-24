import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    client.subscribe(topic="my/topic", qos=1)


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


broker_address = "localhost"
client = mqtt.Client("client_subscribe2")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address)

client.loop_forever()
client.disconnect()
