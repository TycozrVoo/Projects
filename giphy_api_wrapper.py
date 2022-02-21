import requests
from requests.utils import quote
import re
import random


class Giphy:

    def __init__(self, API_KEY):
        self.base_url = "http://api.giphy.com/v1/gifs/"
        self.api_key_param = "api_key="
        self.API_KEY = API_KEY
        self.trending_url = f"{self.base_url}trending?{self.api_key_param}{self.API_KEY}"


    # TRENDING GIF FUNCTIONS
    def get_all_trending_gif_urls(self):
        data = requests.get(self.trending_url).json()
        giphyTrendingURLs = [x for x in re.findall("'url': '(.*?)'", str(data)) if x[:34] != "https://giphy-analytics.giphy.com/"]

        return giphyTrendingURLs


    def get_random_trending_gif_url(self):
        return random.choice(self.get_all_trending_gif_urls())


    def get_first_trending_gif_url(self):
        return self.get_all_trending_gif_urls()[0]


    # GIF SEARCH FUNCTIONS
    def get_all_searched_gif_urls(self, query):
        data = requests.get(f"{self.base_url}search?q={quote(query)}&{self.api_key_param}{self.API_KEY}").json()
        giphySearchedURLs = [x for x in re.findall("'url': '(.*?)'", str(data))]

        return giphySearchedURLs


    def get_random_searched_gif_url(self, query):
        return random.choice(self.get_all_searched_gif_urls(query))


    def get_first_searched_gif_url(self, query):
        return self.get_all_searched_gif_urls(query)[0]


    # RANDOM GIF FUNCTIONS
    def get_all_random_gif_urls(self, query):
        data = requests.get(f"{self.base_url}random?{self.api_key_param}{self.API_KEY}&tag={quote(query)}").json()
        giphyRandomSearchedURLs = [x for x in re.findall("'url': '(.*?)'", str(data))]
        
        return giphyRandomSearchedURLs


    def get_first_random_gif_url(self, query):
        return self.get_all_random_gif_urls(query)[0]
