import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Explicit local backend URL to prevent stale environment variables from breaking requests
backend_url = "http://127.0.0.1:3030"

sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
    
    base_url = backend_url.rstrip('/')
    formatted_endpoint = endpoint if endpoint.startswith('/') else '/' + endpoint
    request_url = base_url + formatted_endpoint + ("?" + params if params else "")
    
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")

def analyze_review_sentiments(text):
    base_url = sentiment_analyzer_url.rstrip('/')
    request_url = base_url + "/analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    base_url = backend_url.rstrip('/')
    request_url = base_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print(f"Network exception occurred: {err}")