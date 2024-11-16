# main.py

import urequests
import boot  # Importing boot.py to access configuration values

def delete_data_from_supabase(user_id):
    # Use the primary key filter with user_id
    url = f"{boot.SUPABASE_BASE_URL}?user_id=eq.{user_id}"
    
    # Headers with the API key and authorization token from boot.py
    headers = {
        "apikey": boot.SUPABASE_API_KEY,
        "Authorization": boot.SUPABASE_AUTH_TOKEN,
        "Prefer": "return=representation"  # Optional: requests Supabase to return the deleted row
    }
    
    try:
        # Send DELETE request to delete the record
        response = urequests.delete(url, headers=headers)
        
        # Check response status
        if response.status_code == 204:
            print("Data deleted successfully in Supabase.")
        elif response.status_code == 200:
            print("Data deleted successfully in Supabase:")
            print("Deleted data:", response.json())
        else:
            print("Failed to delete data in Supabase:", response.status_code, response.text)
    
    except Exception as e:
        print("Failed to delete data from Supabase:", e)

# Run the function with a specific user_id
delete_data_from_supabase(30)
