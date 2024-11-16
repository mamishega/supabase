from mfrc522 import MFRC522
from time import sleep
import boot
import urequests

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

def rfid_post_supabase():
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
                
                url = f"{boot.BASE_URL3}"
                data = {
                    "Scan_Num": card,
                    "full_name": "Mohammed Ali"
                }
                
                header = {
                    "apikey": boot.API_KEY,
                    "Authorization": boot.AUTH_TOKEN
                }
                
                response = urequests.post(url, json=data, headers=header)
                
                if response.status_code in [200, 201]:
                    print("Data posted successfully to Supabase:", data)
                else:
                    print("Failed to post data. Status code:", response.status_code)
                    print("Response:", response.text)
                
                response.close()
            
            sleep(5)
            
        except Exception as e:
            print("Unexpected error:", e)
            sleep(10)

rfid_post_supabase()

