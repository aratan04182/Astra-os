from ai.brain import Brain
from ai.assistant import Assistant

brain = Brain()

assistant = Assistant()

while True:

    command = input(">>> ")

    if command.startswith("learn "):

        text = command.replace("learn ", "")

        brain.learn_text(text)

        print("learnt!!")

    elif command.startswith("ask "):

        question = command.replace("ask ", "")

        print(assistant.ask(question))

    elif command == "exit":

        break
