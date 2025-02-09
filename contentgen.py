import sys
from Xenforo import *
from wonderwords import RandomWord

API_KEY = "7dYIK8dI3tBAkJjBfGl9qHbAl8f6myS3"
API_USER = "Max Power"
BASE_API_URL = "http://127.0.0.1/api"
DEFAULT_PASSWORD = "password"

config = APIConfig(API_KEY, API_USER, BASE_API_URL)
xf = APIEndpoint(config)

r = RandomWord()

# loop from 1 to 10
for i in range(1, 11):
    username_seed = r.word(word_min_length=3, word_max_length=10)
    response = xf.create_registered_user(username_seed)
    if response.status_code != 200:
        print(f"Failed to create user with username seed '{username_seed}'")
        print("Response:", response.json())

