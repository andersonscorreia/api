import requests
YOUR_API_KEY = ''
username= 'andersons.correia'
id = ''
apiVersion = 'v14.0'


r = requests.get(f'https://graph.instagram.com/{apiVersion}/{id}?fields={username}&access_token={YOUR_API_KEY}')
listVideo = r.json()

print(listVideo)
