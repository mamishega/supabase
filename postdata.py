import boot
import urequests


def post_to_supabase():
    url = f"{boot.BASE_URL}"
    data = {
        "firstname": "abc",
        "lastname": "dff",
        "age": "36"
    }
    
    headers = {
        "apikey": boot.API_KEY,
        "Authorization": boot.AUTH_TOKEN
    }
    
    try:
        response = urequests.post(url, json=data, headers=headers)
        print("Data posted to Supabase:")
        print(data)
        
    
    except Exception as e:
        print("Failed to post data to Supabase:", e)



post_to_supabase()

