import requests
YOUR_API_KEY = '645497dbb7d87b72be2bb1aea9218344'
username= 'andersons.correia'
id = '3153832734877241'
apiVersion = 'v14.0'


r = requests.get(f'https://graph.instagram.com/{apiVersion}/{id}?fields={username}&access_token={YOUR_API_KEY}')
listVideo = r.json()

print(listVideo)