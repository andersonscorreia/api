import feedparser,requests,json

url =['https://feeds.folha.uol.com.br/poder/rss091.xml','https://noticias.r7.com/feed.xml','https://feeds.elpais.com/mrss-s/pages/ep/site/brasil.elpais.com/portada']    

TOKEN =  'ccf52e9d36f70b4489020d0f0e076283dd608108'

pesquisa = input('Digite o que deseja:')
materias_feed_lst = []

for i in url:
    materias_feed_dic = feedparser.parse(i)
    materias_feed_lst += materias_feed_dic.entries

     
    for materias in materias_feed_lst: 
        portal = materias_feed_dic['feed']['title']    
        if pesquisa.upper() in materias.title.upper():  

            headers = {
                'Authorization': f'Bearer {TOKEN}',
                'Content-Type': 'application/json',
            }

            data = json.dumps({'long_url': materias.link , "domain": "bit.ly" })

            response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)
            links = response.json()
            links = links['link']
            print(f'PORTAL:{portal}\nTITULO: {materias.title} \nURL:{links}\n')