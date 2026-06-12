from agent.manager import Agent

agent = Agent()

while True:

    goal = input("> ")

    if goal == "exit":

        break

    print(agent.run(goal))
