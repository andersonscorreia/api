import requests
YOUR_API_KEY = ''
SEARCH = 'ifrn'
TYPE = 'video'
RESULT_NUM = '3'




r = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?title&maxResults={RESULT_NUM}&q={SEARCH}%20&type={TYPE}&key={YOUR_API_KEY}')
listVideo = r.json()

print(listVideo)