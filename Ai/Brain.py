from ai.learner import Learner

class Brain:

    def __init__(self):

        self.learner = Learner()

    def learn_text(self, text):

        self.learner.learn(text)
