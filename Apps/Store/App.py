from apps.store.repository import Repository

class Store:

    def __init__(self):

        self.repository = Repository()

    def show(self):

        apps = self.repository.load()

        print()

        print("====== App Store ======")

        for app in apps:

            print(

                app["name"],

                app["version"]

            )

        print()
