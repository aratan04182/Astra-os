import time

from github.update import Update

class Scheduler:

    def __init__(self):

        self.github = Update()

    def start(self):

        while True:

            repos = self.github.list_repositories()

            print("Repository Count:", len(repos))

            time.sleep(3600)
