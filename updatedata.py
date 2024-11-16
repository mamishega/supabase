import urequests
import boot

def update_data_to_supabase(user_id):
    url=f"{boot.BASE_URL}?user_id=eq.{user_id}"
    
    # Data to update
    data = {
        "firstname": "ABC",
        "lastname": "DFF",
        "age": "40"
    }
    
    # Headers with the appropriate API key and authorization token
    headers = {
        "apikey" : boot.API_KEY,
        "Authorization" : boot.AUTH_TOKEN,
        "Prefer": "return=representation"
    }
    
    try:
        # Send PATCH request to update the record
        response = urequests.patch(url, json=data, headers=headers)
        
        # Check response status
        if response.status_code in [200, 204]:
            print("Data updated successfully in Supabase.")
            print("Response data:", response.json())
        else:
            print("Failed to update data in Supabase:", response.status_code, response.text)
    
    except Exception as e:
        print("Failed to post data to Supabase:", e)

# Run the function with a specific user_id
update_data_to_supabase(34)
