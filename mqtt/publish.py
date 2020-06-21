import paho.mqtt.publish as publish
import time

i = 1
while True:
    publish.single("my/topic", "Message: " + str(i), hostname="test.mosquitto.org")
    print("Send message: " + str(i))
    i += 1
    time.sleep(3)
