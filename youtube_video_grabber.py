import requests
import re

"""
A YouTube video grabber that works independent of any web scraping libraries such as bs4
"""

class YouTube:

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

    def video(self, query):
        with requests.session() as s:
            d = s.get(f'https://youtube.com/results?search_query={requests.utils.quote(query)}', headers=self.headers).text
            vidID = re.search('{"videoId":"(.*?)","thumbnail"', d).group(1)
            
        return f'https://youtube.com/watch?v={vidID}'
