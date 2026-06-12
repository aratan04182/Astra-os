from agent.planner import Planner
from agent.executor import Executor
from llm.model import LocalLLM

class Agent:

    def __init__(self):

        self.planner = Planner()

        self.executor = Executor()

        self.model = LocalLLM()

    def run(self, goal):

        plan = self.planner.create_plan(goal)

        self.executor.execute(plan)

        return self.model.generate(goal)
