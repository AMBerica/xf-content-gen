import requests

API_KEY = "7dYIK8dI3tBAkJjBfGl9qHbAl8f6myS3"
API_USER = "Max Power"
BASE_API_URL = "http://127.0.0.1/api"

# Our "surprise" username for this example:
username = "MightyPlatypus9911"
email = "mightyplatypus9911@example.com"

# Construct the URL for creating a user
create_user_endpoint = f"{BASE_API_URL}/users"

# Prepare the data for the new user
payload = {
    "username": username,
    "email": email,
    "password": "SuperSecurePa$$w0rd",  # Replace with a generated or secure password
    "user_group_id": 2,                # Typically "2" is the default Registered Users group
    # Other optional fields can go here, for example:
    # "custom_fields": {
    #     "custom_field_id": "value"
    # }
}

# Set up the headers with your API key
headers = {
    "XF-Api-Key": API_KEY,
    "XF-Api-User": API_USER,
    "Content-Type": "application/x-www-form-urlencoded"
}

# add `api_bypass_permissions=1` to the post payload
payload['api_bypass_permissions'] = 1
response = requests.post(create_user_endpoint, data=payload, headers=headers)

# Print out the response (in JSON format) for debugging
print("Status code:", response.status_code)
print("Response:", response.json())
