import requests
import json

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_output(json_str):
    return json.dumps(json.loads(json_str),indent = 4)

def request_method():
    response = requests.get(build_uri('users/NewerCN'))
    print(better_output(response.text))

if __name__ == '__main__':
    request_method()


