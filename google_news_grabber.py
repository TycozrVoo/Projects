import requests
import re
import random


def news(query):
  headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}

  with requests.session() as n:
    news_data = n.get(f'https://www.google.com/search?q={query}&tbm=nws', headers=headers).text

    news = [article.split('url=')[-1].split('&amp;ved=0ahUKE')[0] for article in re.findall('url=(.*?)&amp;ved=0ahUKE', news_data) if "policies.google.com" not in article and article.startswith('https://') or article.startswith('http://') and not article.endswith('.jpg') and not article.endswith('.png') and not article.endswith('.gif')]

    return random.choice(news)
