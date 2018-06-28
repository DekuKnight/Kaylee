import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print ("Connect with result code: "+str(rc))
    client.subscribe("Kaylee/sys/#")
    client.publish("Kaylee/sys/startup", "Authenticator started")
    client.publish("Kaylee/Notification","remove The front door is unlocked!")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client=mqtt.Client("authenticator")
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

client.loop_forever()

