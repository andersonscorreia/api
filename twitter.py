import requests

username= 'elonmusk'
TOKEN = ''
headers = {
               'Authorization': f'Bearer {TOKEN}',
                'Content-Type': 'application/json',
           }


r = requests.get(f'https://api.twitter.com/2/users/by/username/{username}?user.fields=name%2Cdescription%2Cpublic_metrics%2Cverified%2Clocation',headers = headers )
a =r.json()
print(a)




