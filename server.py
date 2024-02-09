# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
from struct import unpack
from time import sleep

# assinando todas as publica��es dentro da area 10
TOPIC = "area/10/sensor/#"


# fun��o chamada quando a conex�o for realizada, sendo
# ent�o realizada a subscri��o
def on_connect(client, data, rc, properties=None):
    client.subscribe([(TOPIC, 0)])
    print("conectou")


# fun��o chamada quando uma nova mensagem do t�pico � gerada
def on_message(client, userdata, msg, properties=None):
    # decodificando o valor recebido
    v = unpack(">H", msg.payload)[0]
    print(msg.topic + "/" + str(v))


# cria um cliente para supervis�0
client = mqtt.Client(client_id="SCADA",
                     protocol=mqtt.MQTTv31)
# estabelece as fun��e de conex�o e mensagens
client.on_connect = on_connect
client.on_message = on_message

# conecta no broker
client.connect('test.mosquitto.org', 1883)

# permace em loop, recebendo mensagens
client.loop_forever()