import os

class Update:

    def list_repositories(self):

        repos = []

        if not os.path.exists("repositories"):

            os.mkdir("repositories")

        for repo in os.listdir("repositories"):

            repos.append(repo)

        return repos
