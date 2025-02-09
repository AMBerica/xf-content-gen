import requests
import random
random.seed()

API_KEY = "7dYIK8dI3tBAkJjBfGl9qHbAl8f6myS3"
API_USER = "Max Power"
BASE_API_URL = "http://127.0.0.1/api"
PASSWORD = "password"

class APIConfig:
    def __init__(self, api_key, api_user, base_api_url):
        self.api_key = api_key
        self.api_user = api_user
        self.base_api_url = base_api_url

class APIEndpoint:
    def __init__(self, api_config):
        self.api_config = api_config

    def create_registered_user(self, username_seed):
        username = username_seed + str(random.randint(0, 1000000))
        email = username.lower() + "@example.com"
        create_user_endpoint = f"{self.api_config.base_api_url}/users"
        payload = { "api_bypass_permissions": 1, "username": username, "email": email, "password": PASSWORD, "user_group_id": 2,}
        headers = { "XF-Api-Key": API_KEY, "XF-Api-User": API_USER, "Content-Type": "application/x-www-form-urlencoded" }
        return requests.post(create_user_endpoint, data=payload, headers=headers)
    
config = APIConfig(API_KEY, API_USER, BASE_API_URL)
api = APIEndpoint(config)
response = api.create_registered_user("Jeremy")
print("Status code:", response.status_code)
print("Response:", response.json())

# username_seed = "Platypus"
# username = username_seed + str(random.randint(0, 1000000))
# email = username.lower() + "@example.com"

# # Construct the URL for creating a user
# create_user_endpoint = f"{BASE_API_URL}/users"

# Prepare the data for the new user
# payload = {
#     "api_bypass_permissions": 1,
#     "username": username,
#     "email": email,
#     "password": PASSWORD,
#     "user_group_id": 2,
# }

# Set up the headers with your API key
# headers = {
#     "XF-Api-Key": API_KEY,
#     "XF-Api-User": API_USER,
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# add `api_bypass_permissions=1` to the post payload
# payload['api_bypass_permissions'] = 1
# response = requests.post(create_user_endpoint, data=payload, headers=headers)

# Print out the response (in JSON format) for debugging
# print("Status code:", response.status_code)
# print("Response:", response.json())
