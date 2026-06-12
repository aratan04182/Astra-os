class MemoryManager:

    def __init__(self):

        self.memory = []

    def store(self, item):

        self.memory.append(item)

    def search(self, keyword):

        result = []

        for item in self.memory:

            if keyword in item:

                result.append(item)

        return result
