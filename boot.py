# boot.py -- run on boot-up
import network
import time

ssid = "Aussie Broadband 6922"
password = "xacskeyafa"

#ssid = ''
#password = ''

#ssid = ''
#password = ''

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Connected to Wi-Fi", station.ifconfig())


# Supabase API configuration
