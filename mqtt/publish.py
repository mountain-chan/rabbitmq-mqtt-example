import datetime
import random
import time
from urllib.parse import urlparse
from uuid import uuid1
import json

import paho.mqtt.client as mosquitto


class QueueProcessing(object):
    def __init__(self):
        MQTT_TOPIC = "STATUS"
        broker_address = "mqtt://bootai:1234567aA@@192.168.1.57:1883"
        broker_url = urlparse(broker_address)
        mqttc = mosquitto.Client()
        mqttc.username_pw_set(username=broker_url.username, password=broker_url.password)
        mqttc.connect(broker_url.hostname, broker_url.port)

        # Assign event callbacks
        mqttc.on_publish = self.on_publish

        while True:
            MQTT_MSG = json.dumps([{
                "id": str(uuid1()),
                "tag": "FG01:T01:M001_02",
                "type": "Motor",
                "data": {
                    "Running": 0,
                    "Right": 0,
                    "Left": 0,
                    "ServiceEnable": 0,
                    "Simulation": 0,
                    "Fault": random.choice([0, 1]),
                    "Fault_1": 0,
                    "Fault_2": 0,
                    "Fault_3": 0,
                    "Fault_4": 0
                },
                "timestamp": time.time()
            }])
            info_publish = mqttc.publish(topic=MQTT_TOPIC, payload=MQTT_MSG, retain=True)
            print("Sent message: " + str(info_publish.mid), "success: " + str(info_publish.rc))

            MQTT_MSG = json.dumps([{
                "id": str(uuid1()),
                "tag": "FG01:T01:V001_26",
                "type": "Valve",
                "data": {
                    "Opened": 0,
                    "Closed": 0,
                    "ServiceEnable": 0,
                    "Simulation": 0,
                    "Fault": random.choice([0, 1]),
                    "Fault_1": 0,
                    "Fault_2": 0
                },
                "timestamp": time.time()
            }])
            info_publish = mqttc.publish(topic=MQTT_TOPIC, payload=MQTT_MSG, retain=True)
            print("Sent message: " + str(info_publish.mid), "success: " + str(info_publish.rc))

            MQTT_MSG = json.dumps([{
                "id": str(uuid1()),
                "tag": "LEITUNGEN:100:STATUS",
                "type": "Pipeline",
                "data": {"STATUS": random.choice([0, 1, 2])},
                "timestamp": time.time()
            }])
            info_publish = mqttc.publish(topic=MQTT_TOPIC, payload=MQTT_MSG, retain=True)
            print("Sent message: " + str(info_publish.mid), "success: " + str(info_publish.rc))

            MQTT_MSG = json.dumps([{
                "id": str(uuid1()),
                "tag": "FG01:T01:01",
                "type": "FunctionGroups",
                "data": {
                    "GF:StartEnable": 0,
                    "GF:PauseEnable": 0,
                    "GF:StopEnable": 0,
                    "GF:ContinueEnable": 0,
                    "GF:ActiveAndShutdown": 0,
                    "GF:Active": random.choice([0, 1]),
                    "GF:Paused": 0,
                    "GF:Stopped": 0,
                    "GF:End": 0,
                    "GF:StepOn": 0,
                    "GF:StepNo": 0,
                    "GF:StepNoOld": 0,
                    "GF:InformationNo": 0,
                    "S1:ActValue": 0,
                    "S2:ActValue": 0,
                    "S3:ActValue": 0,
                    "S4:ActValue": 0,
                    "S5:ActValue": 0
                },
                "timestamp": time.time()
            }])
            info_publish = mqttc.publish(topic=MQTT_TOPIC, payload=MQTT_MSG, retain=True)
            print("Sent message: " + str(info_publish.mid), "success: " + str(info_publish.rc))

            time.sleep(5)

    def on_publish(self, client, userdata, mid):
        print("Message id: " + str(mid))

    def on_disconnect(self, client, userdata, rc):
        print("client disconnected ok")


if __name__ == '__main__':
    worker = QueueProcessing()
