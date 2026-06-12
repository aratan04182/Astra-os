from ai.brain import Brain
from github.sync import Sync

class System:

    def __init__(self):

        self.brain = Brain()
        self.github = Sync()

    def start(self):

        self.github.update()

        self.brain.initialize()

        while True:

            self.brain.loop()
