import paho.mqtt.subscribe as subscribe

while True:
    msg = subscribe.simple("my/topic", hostname="test.mosquitto.org")
    print("%s %s" % (msg.topic, msg.payload))
