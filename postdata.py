import boot
import urequests


def post_to_supabase():
    url = f"{boot.SUPABASE_BASE_URL}"
    data = {
        "firstname": "Ali",
        "lastname": "Sherif",
        "age": "38"
    }
    
    headers = {
        "apikey": boot.SUPABASE_API_KEY,
        "Authorization": boot.SUPABASE_AUTH_TOKEN
    }
    
    try:
        response = urequests.post(url, json=data, headers=headers)
        print("Data posted to Supabase:")
        print(data)
        
    
    except Exception as e:
        print("Failed to post data to Supabase:", e)



post_to_supabase()

