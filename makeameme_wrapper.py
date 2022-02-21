import requests
import re



class MakeMeme:

  def __init__(self):
    self.headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
    }

    self.meme_ids = {
      "spiderman ok": "390",
      "hospitalized spiderman": "209",
      "spongebob rainbow": "345",
      "tough spongebob": "192",
      "buzz everywhere": "135",
      "y u no": "238",
      "trump says": "448",
      "fry not sure if": "31",
      "fry take my money": "386",
      "jackie chan why": "468",
      "philosoraptor": "6",
      "bench skeleton": "440",
      "stonks": "551",
      "grumpy cat": "22",
      "yay squirrel": "187",
      "think man": "433",
      "boromir explain": "71",
      "zoidberg explains": "91",
      "drunk elsa": "389",
      "its done": "410",
      "sarcastic willy wonka": "127",
      "you were the chosen one": "430",
      "kermit drinking tea": "366",
      "so you're telling me": "63",
      "sarcastic": "315",
      "bad probs": "14",
      "skeptical...": "49",
      "interesting man": "3",
      "minion joy": "382",
      "confession bear": "40"
    }

  def create(self, template, top, bottom):
    if template not in list(self.meme_ids):
      return 'Invalid Template!'

    meme_data = {
      "meme": self.meme_ids[template],
      "top-text": top,
      "bottom-text": bottom,
      "title-text": "CUSTOM MEME",
      "memeIsVisible": 1
    }

    with requests.session() as MEME:
      meme = MEME.post('https://makeameme.org/ajax/createMeme.php', data=meme_data, headers=self.headers).text

      actual_meme = re.search('<meta property="og:image" content="(.*?)" />', meme).group(1)

      return actual_meme
