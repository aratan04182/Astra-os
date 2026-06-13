class Launcher:

    def __init__(self):

        self.apps = {

            "chat": "AI Chat",

            "browser": "Browser",

            "store": "App Store",

            "terminal": "Terminal",

            "files": "Files"

        }

    def home(self):

        print()

        print("📱 AstraAI Home")

        print("----------------")

        for app in self.apps:

            print(app)

        print()

    def run(self, command):

        if command in self.apps:

            print("Opening", self.apps[command])

        else:

            print("Unknown App")
