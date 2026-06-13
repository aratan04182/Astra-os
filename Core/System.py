from ui.launcher import Launcher

class System:

    def __init__(self):

        self.launcher = Launcher()

    def start(self):

        print("Loading System...")

        self.launcher.home()

        while True:

            command = input("> ")

            if command == "exit":

                break

            self.launcher.run(command)
