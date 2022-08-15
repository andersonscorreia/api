import requests
YOUR_API_KEY = ''





r = requests.get(f'https://graph.instagram.com/17896450804038745/children?access_token={YOUR_API_KEY}')
listVideo = r.json()

print(listVideo)