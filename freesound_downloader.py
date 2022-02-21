import requests
import re
import random

class Freesound:

  def __init__(self):
    self.base_url = "https://freesound.org"
    self.browse_url = self.base_url + "/browse"
    self.search_base = self.base_url + "/search/?q="
    self.headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
    }

  def request(self, s=None, isAudioFile=False):
    if (not s) and (not isAudioFile):
      r = requests.get(self.browse_url, self.headers)
      if r.status_code >= 400:
        return False
      else:
        return r.text
    elif s and (not isAudioFile):
      r = requests.get(self.search_base + s, self.headers)
      if r.status_code >= 400:
        return False
      else:
        return r.text
    else:
      r = requests.get(s, self.headers)
      if r.status_code >= 400:
        return False
      else:
        return r.content

  def download(self, url, name):
    content = self.request(url, True)
    with open(f"{name}.mp3", "wb+") as f:
      f.write(content)

  def debug(self, options):
    if (options["mode"].lower() == "w") and options["data"]:
      with open("debug.txt", "w+") as f:
        f.write(options["data"])
    elif (options["mode"].lower() == "r"):
      with open("debug.txt", "r") as f:
        return f.readlines()

  def search(self, data):
    path = re.search('<a class="mp3_file" href="(.*?)" title="mp3 file">', data).group(1)
    name = re.search('title="mp3 file">(.*?)</a>', data).group(1)

    return path, name

  def findall(self, data):
    path = re.findall('<a class="mp3_file" href="(.*?)" title="mp3 file">', data)
    name = re.findall('title="mp3 file">(.*?)</a>', data)

    return path, name
    
  def getSound(self, query):
    r = self.request(query)
    if r:
      path, name = self.search(r)
      return {
        "url": self.base_url + path,
        "name": name
      }
    else:
      return False

  def getRandom(self, query):
    r = self.request(query)
    if r:
      rand = random.randint(0, len(self.findall(r)[0]))

      try:
        path, name = self.findall(r)[0][rand], self.findall(r)[1][rand]
      except:
        path, name = self.findall(r)[0][rand], self.findall(r)[1][rand]
        
      return {
        "url": self.base_url + path,
        "name": name
      }
    else:
      return False

  def soundOfTheDay(self):
    r = self.request()
    if r:
      self.debug({
        "data": r,
        "mode": "w"
      })
      src = self.debug({
        "mode": "r"
      })
  
      try:
        select1 = src.index('''        <h3>Random sound of the day</h3>\n''')
        select2 = src.index("    </div><!-- #sound_of_the_day -->\n")
      except:
        return False
  
      text = "".join(src[select1: select2 + 1])
      path, name = self.search(text)
      return {
        "url": self.base_url + path,
        "name": name
      }
    else:
      return False

  def recent(self):
    r = self.request()
    if r:
      self.debug({
        "data": r,
        "mode": "w"
      })
      src = self.debug({
        "mode": "r"
      })

      try:
        select1 = src.index("    <h3>Recent Additions</h3>\n")
        select2 = src.index('    <p class="more_button" ><a href="/search/?q=&f=&s=created+desc">more...</a></p>\n')
      except:
        return False

      text = "".join(src[select1: select2 + 1])
      path, name = self.search(text)
      return {
        "url": self.base_url + path,
        "name": name
      }
    else:
      return False

  def random(self):
    r = self.request()
    if r:
      self.debug({
        "data": r,
        "mode": "w"
      })
      src = self.debug({
        "mode": "r"
      })

      try:
        select1 = src.index("    <h3>Recent Additions</h3>\n")
        select2 = src.index('    <p class="more_button" ><a href="/search/?q=&f=&s=created+desc">more...</a></p>\n')
      except:
        return False

      text = "".join(src[select1: select2 + 1])
      rand = random.randint(0, len(self.findall(r)[0]))

      try:
        path, name = self.findall(text)[0][rand], self.findall(r)[1][rand]
      except:
        path, name = self.findall(r)[0][rand], self.findall(r)[1][rand]
      return {
        "url": self.base_url + path,
        "name": name
      }
    else:
      return False
