import datetime
from urllib.parse import urlparse
import paho.mqtt.client as mosquitto
import json


class QueueProcessing(object):
    def __init__(self):
        MQTT_TOPIC = "STATUS"
        broker_address = "paho_mqtt://bootai:1234567aA@@192.168.1.57:1883"
        broker_url = urlparse(broker_address)
        mqttc = mosquitto.Client()
        mqttc.username_pw_set(username=broker_url.username, password=broker_url.password)
        mqttc.connect(broker_url.hostname, broker_url.port)

        # Assign event callbacks
        mqttc.on_connect = self.on_connect
        mqttc.on_message = self.on_message

        mqttc.loop_forever()

    # Define event callbacks
    def on_connect(self, client, userdata, flags, rc):
        client.subscribe(topic="STATUS")

    def on_message(self, client, userdata, message):
        payload = json.loads(message.payload)
        print(payload)


if __name__ == '__main__':
    worker = QueueProcessing()

