class KnowledgeGraph:

    def __init__(self):

        self.nodes = {}

    def add(self, title, data):

        self.nodes[title] = data

    def search(self, title):

        return self.nodes.get(title)
