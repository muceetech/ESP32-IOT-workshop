import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

# Setup Wi-Fi and MQTT
# Connect to WiFi

WIFI_SSID = ""
WIFI_PASS = ""
MQTT_BROKER = "broker.hivemq.com"
MQTT_CLIENT_ID = "esp32-traffic"
MQTT_TOPIC = b"esp/led"

# Pins for Red, Yellow, Green LEDs
led = Pin(4, Pin.OUT)

led.value(0)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)
    while not wlan.isconnected():
        time.sleep(0.2)
    print("WiFi Connected!")

def handle_message(topic, msg):
    value1 = msg.decode()
    print("value", value1)
    led.value(0)
    if value1 == "on":
        led.value(1)
    elif value1 == "off":
        led.value(0)

def main():
    connect_wifi()
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER)
    client.set_callback(handle_message)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Connected to MQTT broker")

    while True:
        client.check_msg()
        time.sleep(0.1)

main()

