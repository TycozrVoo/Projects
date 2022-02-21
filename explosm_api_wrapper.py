import requests
from PIL import Image
from io import BytesIO


def get_panels():
  data = requests.get("https://explosm.net/api/get-random-panels").json()["panels"][:3]
  return ["https://rcg-cdn.explosm.net/panels/" + comic["filename"] for comic in data]

def generate_images():
  container = [Image.open(BytesIO(requests.get(link).content)) for link in get_panels()]
  width, height = container[0].size
  
  result = Image.new('RGB', (width*3, height))

  result.paste(container[0], (0, 0))
  result.paste(container[1], (container[0].width, 0))
  result.paste(container[2], (container[0].width*2, 0))
  result.save("explosm.png")
