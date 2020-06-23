# import paho.mqtt.subscribe as subscribe
#
# while True:
#     msg = subscribe.simple("my/topic", hostname="localhost")
#     print("%s %s" % (msg.topic, msg.payload))

import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(topic="my/topic")


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    # print("message topic=", message.topic)
    # print("message qos=", message.qos)
    # print("message retain flag=", message.retain)


broker_address = "localhost"
# broker_address = "iot.eclipse.org"
# broker_address = "test.mosquitto.org"

client = mqtt.Client("client_subscribe2")  # create new instance
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_address)  # connect to broker

client.loop_forever()
client.disconnect()
