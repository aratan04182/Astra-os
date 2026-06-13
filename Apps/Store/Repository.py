import json

class Repository:

    def load(self):

        with open("store.json","r") as file:

            return json.load(file)
