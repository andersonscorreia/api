import requests
YOUR_API_KEY=''
company = 'star wars'

r = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={YOUR_API_KEY}&page=1&query={company}&year=2022')
listVideo = r.json()
print(listVideo)