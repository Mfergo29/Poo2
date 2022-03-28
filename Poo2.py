from urllib import request


import requests

class Words:
    def __init__(language):
        language='en'

r=requests.get('https://random-word-api.herokuapp.com/')
print(r)

