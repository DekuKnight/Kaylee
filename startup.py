import authenticator, dummy
import paho.mqtt.client as mqtt
import threading

client=mqtt.Client()
client.on_connect = authenticator.on_connect
client.on_message = authenticator.on_message

client.connect("test.mosquitto.org", 1883, 60)

t = threading.Thread(target=client.loop_forever)
t.start()

dummyclient= mqtt.Client()
dummyclient.on_connect = dummy.on_connect
dummyclient.on_message = dummy.on_message

dummyclient.connect("test.mosquitto.org", 1883, 60)

t = threading.Thread(target=dummyclient.loop_forever)
t.start()