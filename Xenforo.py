import random
import requests

DEFAULT_USER_PASSWORD = "password"

class APIConfig:
    def __init__(self, api_key, api_user, base_api_url):
        self.api_key = api_key
        self.api_user = api_user
        self.base_api_url = base_api_url

class APIEndpoint:
    def __init__(self, api_config):
        self.config = api_config
        random.seed()

    def create_registered_user(self, username_seed, password=DEFAULT_USER_PASSWORD):
        username = username_seed + f"{random.randint(0, 100):03}"
        email = username.lower() + "@example.com"
        print(f"Creating user with username '{username}' and email '{email}'")
        create_user_endpoint = f"{self.config.base_api_url}/users"
        payload = { "api_bypass_permissions": 1, "username": username, "email": email, "password": password, "user_group_id": 2,}
        headers = { "XF-Api-Key": self.config.api_key, "XF-Api-User": self.config.api_user, "Content-Type": "application/x-www-form-urlencoded" }
        return requests.post(create_user_endpoint, data=payload, headers=headers)
    