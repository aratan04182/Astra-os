from ai.memory import Memory

class Assistant:

    def __init__(self):

        self.memory = Memory()

        self.memory.load()

    def ask(self, question):

        result = self.memory.search(question)

        if len(result) == 0:

            return "Sorry I dont know:"

        return result[:5]
