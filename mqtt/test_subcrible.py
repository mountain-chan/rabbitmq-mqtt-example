import timeit

long = timeit.timeit('client.loop_forever()',
              setup='import paho.mqtt.client as mqtt; broker_address = "localhost"; client = mqtt.Client(client_id="client_publish"); client.connect(broker_address);client.loop_start()',
              number=1)

print(long)
