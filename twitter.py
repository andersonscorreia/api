import requests
YOUR_API_KEY = ''
username= 'isaac_luis2012'
TOKEN = ''
headers = {
               'Authorization': f'Bearer {TOKEN}',
                'Content-Type': 'application/json',
           }


r = requests.get(f'https://api.twitter.com/2/users/by/username/{username}?user.fields=name%2Cdescription%2Cpublic_metrics%2Cverified',headers = headers )
a =r.json()
print(a)




