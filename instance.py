import paho.mqtt.client as mqttClient
import time


def on_connect(client, userdata, flags, rc):

    if rc == 0:

        print("Соединение с MQTT брокером")
        global Connected
        Connected = True

    else:
        print("Соединение сброшено")


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print(m_decode)


Connected = False

brokerAddress = ""     # Адресс MQTT сервера
port = 0                            # Порт MQTT брокера
user = ""                       # Логин пользователя
password = ""               # Пароль пользователя
topicName = ""                  # Название топика

client = mqttClient.Client("Python")
client.username_pw_set(user, password=password)
client.on_connect = on_connect
client.on_message = on_message

client.connect(brokerAddress, port=port)

client.loop_start()

while Connected is not True:
    time.sleep(0.1)

client.subscribe(topicName)

iprev = 0

for i in range(0, 10):
    client.publish(topicName, iprev)
    time.sleep(2)
    if iprev == 0:
        iprev = 1
    else:
        iprev = 0

time.sleep(4)

print("Закрытие соединения")
client.loop_stop()
client.disconnect()
