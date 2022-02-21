import requests
import json


class Wrapper:

  def __init__(self):
    self.base_url = "https://boredapi.com/api/activity"

  # Private helper used for getting pseudo random data
  def _get_full_random_activity_response(self):
    r = requests.get(self.base_url)

    return r.json()

  def get_random_activity(self):
    r = requests.get(self.base_url)

    return r.json()["activity"]

  def get_activity_by_key(self, key):
    r = requests.get(f"{self.base_url}?key={key}")

    return r.json()["activity"]

  def get_activity_by_random_key(self):
    r = requests.get(f"{self.base_url}?key=" + self._get_full_random_activity_response()["key"])

    return r.json()["activity"]

  def get_activity_by_type(self, _type):
    r = requests.get(f"{self.base_url}?type={_type}")

    return r.json()["activity"]

  def get_activity_by_random_type(self):
    r = requests.get(f"{self.base_url}?type=" + self._get_full_random_activity_response()["type"])

    return r.json()["activity"]

  def get_activity_by_number_participants(self, num: str):
    r = requests.get(f"{self.base_url}?participants={num}")

    return r.json()["activity"]
  
  def get_activity_by_random_number_participants(self):
    r = requests.get(f"{self.base_url}?participants=" + self._get_full_random_activity_response()["participants"])

    return r.json()["activity"]

  def get_activity_by_price(self, price: str):
    r = requests.get(f"{self.base_url}?price={price}")

    return r.json()["activity"]

  def get_activity_by_random_price(self):
    r = requests.get(f"{self.base_url}?price=" + self._get_full_random_activity_response()["price"])

    return r.json()["activity"]

  def get_activity_by_min_max_price(self, min: str, max: str):
    r = requests.get(f"{self.base_url}?minprice={min}&maxprice={max}")

    return r.json()["activity"]

  def get_activity_by_accessibility(self, accessibility: str):
    r = requests.get(f"{self.base_url}?accessibility={accessibility}")

    return r.json()["activity"]

  def get_activity_by_min_max_accessibility(self, min: str, max: str):
    r = requests.get(f"{self.base_url}?minaccessibility={min}?maxaccessibility={max}")

    return r.json()["activity"]
