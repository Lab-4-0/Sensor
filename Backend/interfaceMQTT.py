from paho.mqtt import client as mqtt_client
import random, threading

# Config Broker MQTT:
broker = '192.168.0.66'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 100)}'

# Conexao ao Broker:
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print('Connectado ao MQTT Broker!')
        else:
            print(f'Falha ao conectar! Erro: ({rc})')

    client = mqtt_client.Client(client_id)
    client.username_pw_set(None) #(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

# Inscricao de topico:
def subscribe(client: mqtt_client, topic: str()):
    
    def on_message(client, userdata, msg):
        print(f'Topico: {msg.topic}')
        print(f'Mensagem recebida: {msg.payload.decode()}')
        return str(msg.payload.decode())

    client.subscribe(topic)
    client.on_message = on_message
    
    
#Teste:
if __name__ == '__main__':
    client = connect_mqtt()
    subscribe(client, 'testes/001')
    subscribe(client,'testes/002')
   
    t01 = threading.Thread(target=client.loop_forever)
    t01.start()