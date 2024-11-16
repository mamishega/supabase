# boot.py -- run on boot-up
import network
import time

ssid = "Aussie Broadband 6922"
password = "xacskeyafa"

#ssid = 'AndriodAP635'
#password = 'Moh220582'

#ssid = 'CyFi'
#password = 'SecurityA40'

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while not station.isconnected():
    print("Connecting to Wi-Fi...")
    time.sleep(1)

print("Connected to Wi-Fi", station.ifconfig())


# Supabase API configuration
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRxenR2Zm9ka3h2dmZwcnlzbHdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE0NTYxNTcsImV4cCI6MjA0NzAzMjE1N30.S1mFCvUvKGUSCkHeP-VmQiEcwQ-3hxbZ2fcf2cpgjDI"
AUTH_TOKEN = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRxenR2Zm9ka3h2dmZwcnlzbHdjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzE0NTYxNTcsImV4cCI6MjA0NzAzMjE1N30.S1mFCvUvKGUSCkHeP-VmQiEcwQ-3hxbZ2fcf2cpgjDI"
BASE_URL = "https://tqztvfodkxvvfpryslwc.supabase.co/rest/v1/Users"
BASE_URL2 = "https://tqztvfodkxvvfpryslwc.supabase.co/rest/v1/TemperaturAndHumidity"
BASE_URL3 = "https://tqztvfodkxvvfpryslwc.supabase.co/rest/v1/RfidScan"