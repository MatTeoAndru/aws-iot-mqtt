import time
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


def customCallback(client, userdata, message):
    print("Messaggio in entrata...")
    payload = json.loads(message.payload.decode())
    print(payload)
    
    if payload["message"] == "riavvia macchina":
        print("riavvio macchina in corso ...")

        print("riavvio macchina avvenuto con successo")



myMQTTClient = AWSIoTMQTTClient("dojodevice1")
myMQTTClient.configureEndpoint("a3byfosjxlrb2m-ats.iot.eu-central-1.amazonaws.com", 8883)
myMQTTClient.configureCredentials("./AmazonRootCA1.pem","./055834d4acfe1272258864ee1e86a55cedeb40724bf5459dc0c6f718c9278330-private.pem.key", "./055834d4acfe1272258864ee1e86a55cedeb40724bf5459dc0c6f718c9278330-certificate.pem.crt")

myMQTTClient.connect()
print("Client connesso, in ascolto")

myMQTTClient.subscribe("general/outbound", 1, customCallback)
print('In attesa della callback. Clicca per continuare')
x = input()

myMQTTClient.unsubscribe("general/outbound")
print("Client unsubscribed") 


myMQTTClient.disconnect()
print("Client Disconnected")