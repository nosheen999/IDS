
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
imdb_url = "https://www.imdb.com/search/title/?groups=top_100&ref_=adv_prv"


headers = {"Accept-Language": "en-US, en;q=0.5"}
results = requests.get(imdb_url, headers=headers)
movie_soup = BeautifulSoup(results.text, "html.parser")
movie_name = []
imdb_ratings = []
movie_div = movie_soup.find_all('div', class_='lister-item mode-advanced')
for container in movie_div[:5]:

        name = container.h3.a.text
        movie_name.append(name)

        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
        time.sleep(1)
movies = pd.DataFrame({
'movie_name': movie_name,
'imdb_ratings': imdb_ratings
})

movies.to_excel('top_5_movies.xlsx', index=False)