import requests
import re
import random


class GoogleVids:
  
  def __init__(self):
    self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
  
  def first_video(self, query):

    data = requests.get(f'https://www.google.com/search?q={query}&tbm=vid', headers=self.headers).text

    vid = re.search('<div class="yuRUbf"><a href="(.*?)"', data).group(1)

    data2 = requests.get(vid, headers=self.headers).text

    thumbnail = re.search('<link itemprop="thumbnailUrl" href="(.*?)">', data2).group(1)

    return f'''
VIDEO LINK: {vid}
THUMBNAIL: {thumbnail}
  '''

  def random_video(self, query):

    data = requests.get(f'https://www.google.com/search?q={query}&tbm=vid', headers=self.headers).text

    video_container = [x for x in re.findall('<div class="yuRUbf"><a href="(.*?)"', data) if x.startswith('https://www.youtube.com/')]

    random.shuffle(video_container)
    rand_video = random.choice(video_container)

    data2 = requests.get(rand_video, headers=self.headers).text

    thumbnail = "".join([x for x in re.search('<link itemprop="thumbnailUrl" href="(.*?)">', data2).group(1) if len(x) <= 52 and not x.startswith('https://yt3.gght.com')]) 

    return f'''
VIDEO LINK {rand_video}
THUMBNAIL: {thumbnail}
  '''
