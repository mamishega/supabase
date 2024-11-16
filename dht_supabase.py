from machine import Pin
from time import sleep
import dht
import boot
import urequests

DHT = dht.DHT11(Pin(2))

def post_to_supabase():
    while True:
        try:
            DHT.measure()
            temperature = DHT.temperature()
            humidity = DHT.humidity()
            #print("Temperature:", temperature, "Humidity:", humidity)
            
            url = f"{boot.BASE_URL2}"
            data = {
                "temperature": temperature,
                "humidity": humidity
            }
            
            headers = {
                "apikey": boot.API_KEY,
                "Authorization": boot.AUTH_TOKEN
            }
            
            response = urequests.post(url, json=data, headers=headers)
            
                
            if response.status_code in [200, 201]:
                print("Data posted successfully to Supabase:", data)
                
            else:
                print("Failed to post data. Status code:", response.status_code)
                print("Response:", response.text)
            
            response.close()
            sleep(60)  
            
        
        except Exception as e:
            print("Unexpected error:", e)
            sleep(10)

post_to_supabase()
