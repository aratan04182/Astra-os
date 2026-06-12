from ai.learner import Learner
from ai.search import Search

learner = Learner()

learner.learn(
    "https://github.com/pallets/flask.git"
)

assistant = Search()

while True:

    question = input("> ")

    print(
        assistant.ask(question)
    )
