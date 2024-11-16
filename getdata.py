import boot
import urequests

def fetch_data(user_id):
   
    url = f"{boot.BASE_URL}?user_id=eq.{user_id}"
    
    try:
        
        
        # Supabase request headers with API key
        headers = {
            "apikey": boot.API_KEY,
            "Authorization": boot.AUTH_TOKEN
        }
        response = urequests.get(url, headers=headers)
        data = response.json()
        
        print("Data received from Supabase (PostGrest):")
        print(data)
    
    except Exception as e:
        print("Failed to fetch data:", e)




# Run the functions
fetch_data(31)



