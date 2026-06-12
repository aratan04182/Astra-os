from ai.reasoning import Reasoning
from ai.memory import Memory

class Learner:

    def __init__(self):

        self.reasoning = Reasoning()

        self.memory = Memory()

        self.memory.load()

    def learn(self, code):

        result = self.reasoning.analyze(code)

        self.memory.add(str(result))
