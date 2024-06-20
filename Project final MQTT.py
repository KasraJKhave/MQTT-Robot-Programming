# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 14:58:01 2023

@author: Kasra
"""

import paho.mqtt.publish as mqtt_publish
from paho.mqtt import client as mqtt_client
def main():
    #Initialize Parameters
    mqtt_host_address = '192.168.10.121'
    mqtt_port = 1883
    mqtt_keep_alive = 60
    mqtt_ca_cert = 'root.ca'
    mqtt_certfile = 'cq.crt'
    mqtt_keyfile = 'c1.key'
    
    #Initialize MQTT Client
    client = mqtt_client.Client()
    client.on_message = on_message
    client.on_publish = on_publish
    
    client.connect(mqtt_host_address, mqtt_port, mqtt_keep_alive)
    client.subscribe("devices/io-expander/1/digital-input/3", 0)
    
    publish_msg("{'devices/io-expander/1/digital-input/3':8}", mqtt_host_address)
   
   
    while True:
        client.loop()

def on_message(client, userdata, message):
    print("message topic: {}".format(message.topic))
    m_decode = str(message.payload.decode("utf-8","ignore"))
    print("message payload: {}".format(m_decode))
    
def on_publish(mosq, obj, mid):
    print("on_publish, mid{}".format(mid))

def publish_msg(payload_msg, mqtt_host_address):
    mqtt_publish.single(topic='devices/io-expander/1/digital-input/3', payload=input(), hostname=mqtt_host_address)

if __name__ == "__main__":
    main()    
    

    