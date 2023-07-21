import json
import random
import sys
import ssl
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import unicodedata


deviceName = "dojodevice1"
mqttc = AWSIoTMQTTClient("dojodevice1")

mqttc.configureEndpoint("a3byfosjxlrb2m-ats.iot.eu-central-1.amazonaws.com", 8883)
mqttc.configureCredentials("./AmazonRootCA1.pem", "./055834d4acfe1272258864ee1e86a55cedeb40724bf5459dc0c6f718c9278330-private.pem.key", "./055834d4acfe1272258864ee1e86a55cedeb40724bf5459dc0c6f718c9278330-certificate.pem.crt")

with open('allarmi.json', 'r') as json_file:
    data = json.load(json_file)

choices = [False] * 99 + [True] * 1  

def json_encodealarm(string):
    return json.dumps(string)

mqttc.json_encodealarm = json_encodealarm


mqttc.connect()
print("Connected")

#Generazione Allarmi
for item in data:
    item['Device'] = deviceName
    item['Tipologia'] = random.choice(choices)

    message = mqttc.json_encodealarm(item)
    mqttc.publish("general/alarm", message, 1)
    print("Message published. Data:" + message)

print("Sending to IoT Core")

mqttc.disconnect()
time.sleep(2)


print(json.dumps(data, indent=4))


with open('analogicoA.json', 'r') as json_file:
    analog_values = json.load(json_file)



def json_encodeTypeA(string):
    return json.dumps(string, ensure_ascii=False)

mqttc.json_encodeTypeA = json_encodeTypeA

mqttc.connect()
print("Connected")

#Type A analogico
for x, item in enumerate(data):
    # Genera i valori casuali per i campi 'val1', 'val2', 'val3' e 'message'
    analogico_values = random.choice(analog_values)
    codice = analogico_values["Codice"]
    descrizione = unicodedata.normalize('NFKD', analogico_values["Descrizione"]).encode('ascii', 'ignore').decode('ascii')
    tipologia = analogico_values["Tipologia"]
    message = {
        'val1': "{} - {}".format(descrizione, x + 1),
        'val2': "{} - {}".format(descrizione, x + 1),
        'val3': "{} - {}".format(descrizione, x + 1),
        'message': "Test Message - {}".format(x + 1),
        'SeqNumber': x,
        'SeqSort': 1
    }
    message = mqttc.json_encodeTypeA(message)
    mqttc.publish("general/inbound", message, 1)
    print("Message {} published. Data: {}".format(x + 1, message))

print("Sending to IoTCore")
mqttc.disconnect()
time.sleep(2)




#BooleanA
with open('BooleanA.json', 'r') as json_file:
    data = json.load(json_file)

choices = [False] * 99 + [True] * 1  

def json_encodeBooleanA(string):
    return json.dumps(string)

mqttc.json_encodeBooleanA = json_encodeBooleanA


mqttc.connect()
print("Connected")

#Generazione Allarmi
for item in data:
    item['Device'] = deviceName
    item['Tipologia'] = random.choice(choices)

    message = mqttc.json_encodeBooleanA(item)
    mqttc.publish("general/inbound", message, 1)
    print("Message published. Data:" + message)

print("Sending to IoT Core")

mqttc.disconnect()
time.sleep(2)


print(json.dumps(data, indent=4))
