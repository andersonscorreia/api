import requests
YOUR_API_KEY = ''
SEARCH = 'ifrn'
TYPE = 'video'
RESULT_NUM = '10'


r = requests.get(f'https://youtube.googleapis.com/youtube/v3/search?title&maxResults={RESULT_NUM}&q={SEARCH}%20&type={TYPE}&key={YOUR_API_KEY}')
listVideo = r.json()
lista = listVideo['items']
listId = [] 
videos = '\n'
for i in lista:
    
  a = i['id']['videoId']
  listId.append(a) 
for ID in listId:    
    p = requests.get(f'https://youtube.googleapis.com/youtube/v3/videos?part=snippet&id={ID}&key={YOUR_API_KEY}')
    descri = p.json()    
   
    for i in descri['items']:           
        canal = i['snippet']['channelTitle']
        titulo = i['snippet']['title']
        link = f'https://www.youtube.com/watch?v={ID}'
        videos += (f'Canal: {canal}\nTítulo: {titulo}\nLink: {link}\n\n') 
print(videos)