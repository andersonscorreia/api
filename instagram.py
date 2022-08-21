
import requests,os
YOUR_API_KEY = ''
username= 'Casimiro'


bearer_token = os.environ.get("BEARER_TOKEN")
r = requests.get(f'https://api.twitter.com/2/tweets/search/recent')
print(r)