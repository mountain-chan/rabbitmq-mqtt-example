import paho.mqtt.client as mqtt


broker_address = "localhost"

client = mqtt.Client(client_id="client_publish")
client.connect(broker_address)  # connect to broker
client.loop_start()


def ex1():
    i = 0
    while i < 100000:
        client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
        i += 1


def ex2():
    for i in range(100000):
        client.publish(topic="my/topic", payload="Message: " + str(i), retain=True)
