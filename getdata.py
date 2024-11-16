import boot
import urequests

def fetch_data():
   
    url = f"{boot.SUPABASE_BASE_URL}"
    
    try:
        
        
        # Supabase request headers with API key
        headers = {
            "apikey": boot.SUPABASE_API_KEY        }
        response = urequests.get(url, headers=headers)
        data = response.json()
        
        print("Data received from Supabase (PostGrest):")
        print(data)
    
    except Exception as e:
        print("Failed to fetch data:", e)



fetch_data()



