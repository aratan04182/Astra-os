from ai.thinker import Thinker
from ai.summarizer import Summarizer
from ai.memory_manager import MemoryManager

class Brain:

    def __init__(self):

        self.thinker = Thinker()
        self.summarizer = Summarizer()
        self.memory = MemoryManager()

    def process(self, text):

        idea = self.thinker.analyze(text)

        summary = self.summarizer.create(idea)

        self.memory.store(summary)

        return summary
