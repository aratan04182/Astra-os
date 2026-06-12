from github.collector import Collector
from github.parser import Parser
from memory.vector import save

class Learner:

    def __init__(self):

        self.collector = Collector()

        self.parser = Parser()

    def learn(self, repo):

        folder = self.collector.clone(repo)

        texts = self.parser.read(folder)

        for index, text in enumerate(texts):

            save(text, index)
