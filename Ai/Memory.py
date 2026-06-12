import json

class Memory:

    def __init__(self):

        self.file = "knowledge/memory.json"

        self.data = []

    def load(self):

        try:

            with open(self.file, "r") as f:

                self.data = json.load(f)

        except:

            self.data = []

    def save(self):

        with open(self.file, "w") as f:

            json.dump(self.data, f)

    def add(self, text):

        self.data.append(text)

        self.save()

    def search(self, keyword):

        result = []

        for item in self.data:

            if keyword.lower() in item.lower():

                result.append(item)

        return result
