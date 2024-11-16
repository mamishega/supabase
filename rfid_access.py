from mfrc522 import MFRC522
from time import sleep
import boot
import urequests
from machine import Pin

# RFID Reader setup
reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

# RGB LED setup with new GPIO pin assignments
red_led = Pin(16, Pin.OUT)
green_led = Pin(17, Pin.OUT)



red_led.off()
green_led.off()
def rfid_check_database():
    while True:
        try:
            print("Bring TAG closer...")
            print("")
            
            reader.init()
            (stat, tag_type) = reader.request(reader.REQIDL)
            card = None  
            
            if stat == reader.OK:
                (stat, uid) = reader.SelectTagSN()
                if stat == reader.OK:
                    card = int.from_bytes(bytes(uid), "little", False)
                    print("CARD ID: " + str(card))
            
            if card is not None:  
                
                # Check if the RFID is in the database
                url = f"{boot.BASE_URL3}?Scan_Num=eq.{card}"
                
                header = {
                    "apikey": boot.API_KEY,
                    "Authorization": boot.AUTH_TOKEN
                }
                
                response = urequests.get(url, headers=header)
                
                if response.status_code == 200 and response.json():
                    # Card found in the database
                    print("Card is authorized")
                    #set_led_color(0, 1, 0)  # Green ON, Red OFF, Blue OFF
                    green_led.on()
                    red_led.off()
                    sleep(2)
                    green_led.off()
                    sleep(3)
                else:
                    # Card not found in the database
                    print("Card is unauthorized")
                    #set_led_color(1, 0, 0)  # Green OFF, Red ON, Blue OFF
                    red_led.on()
                    green_led.off()
                    sleep(2)
                    red_led.off()
                    sleep(3)
                response.close()
            
            
            
            sleep(5)
            
        except Exception as e:
            print("Unexpected error:", e)
            #set_led_color(0, 0, 0)  # Turn off all LEDs
            sleep(6)

rfid_check_database()
