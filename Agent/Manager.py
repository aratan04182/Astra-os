from agent.planner import Planner
from agent.executor import Executor

class Agent:

    def __init__(self):

        self.planner = Planner()

        self.executor = Executor()

    def execute(self, goal):

        plan = self.planner.create(goal)

        return self.executor.run(plan)
