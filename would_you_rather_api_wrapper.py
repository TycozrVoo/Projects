import requests


class WouldYouRather:

    def __init__(self):
        self.base_url = "https://would-you-rather-api.abaanshanid.repl.co"

    def getRandomQuestion(self):
        data = requests.get(self.base_url).json()

        return data["data"]

    def getQuestionById(self, id):
        if not id:
            return False
        
        try:
            data = requests.get(self.base_url + f"?id={id}").json()

            return data["data"]
        except Exception as e:
            print(f"Exception occured: {e}")

    def getAllQuestions(self):
        for id in range(0, 120):
            print(requests.get(self.base_url + f"?id={id}").json()["data"])
