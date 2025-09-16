import requests

def GetStatus(url):
    return requests.get(url).status_code
