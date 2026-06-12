class History:

    def __init__(self):

        self.logs = []

    def save(self, message):

        self.logs.append(message)

    def recent(self):

        return self.logs[-10:]
