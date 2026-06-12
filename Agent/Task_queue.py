class TaskQueue:

    def __init__(self):

        self.tasks = []

    def add(self, task):

        self.tasks.append(task)

    def next(self):

        if len(self.tasks) == 0:

            return None

        return self.tasks.pop(0)
