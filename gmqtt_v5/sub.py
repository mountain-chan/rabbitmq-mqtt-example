import asyncio
import time
from urllib.parse import urlparse

from gmqtt import Client as MQTTClient

STOP = asyncio.Event()

count = 1


def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('TEST/T1', qos=1)


def on_message(client, topic, payload, qos, properties):
    global count
    print('RECV MSG:', payload)
    print(count)
    count += 1


def on_disconnect(client, packet, exc=None):
    print('Disconnected')


def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')


def ask_exit(*args):
    STOP.set()


async def main(broker_host, username, password):
    client = MQTTClient(client_id="sub-client-id", receive_maximum=24000, clean_session=False,
                        session_expiry_interval=60)

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe

    client.set_auth_credentials(username=username, password=password)
    await client.connect(broker_host)
    await STOP.wait()
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    broker_address = "paho_mqtt://bootai:1234567aA@@localhost:1883"
    broker_url = urlparse(broker_address)
    loop.run_until_complete(main(broker_url.hostname, broker_url.username, broker_url.password))
