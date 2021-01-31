import paho.mqtt.client as mqtt
import json
from tinydb import TinyDB

# uncomment for deta support
#from db import *

#tinydb setup
db1 = TinyDB('db.json')

# MQTT Host
MQTT_HOST = 'test.mosquitto.org'

# Topic to subscribe
TOPIC = 'test/owntracks'

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    msg.payload = msg.payload.decode("utf-8")
    try:
        data = json.loads(msg.payload)
        db1.update(data)
        print('done')
    except:
        print('error')
        print(msg.payload)

# uncomment for deta suppport
# def on_message(mqttc, obj, msg):
#     print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
#     msg.payload = msg.payload.decode("utf-8")
#     try:
#         data = json.loads(msg.payload)
#         db.update(data, BaseKey)
#         print('done')
#     except:
#         print('error')
#         print(msg.payload)


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


# If you want to use a specific client id, use
# mqttc = mqtt.Client("client-id")
# but note that the client id must be unique on the broker. Leaving the client
# id parameter empty will generate a random id for you.
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
# mqttc.on_log = on_log
mqttc.connect(MQTT_HOST, 1883, 60)
mqttc.subscribe(TOPIC, 0)

mqttc.loop_forever()
