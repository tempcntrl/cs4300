# Get requests
import requests

# Use requests to get info from url
def GetStatus(url):
    return requests.get(url).status_code
