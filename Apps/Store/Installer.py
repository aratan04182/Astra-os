import json

class Installer:

    def install(self,app):

        try:

            with open("installed.json","r") as file:

                installed = json.load(file)

        except:

            installed = []

        if app not in installed:

            installed.append(app)

        with open("installed.json","w") as file:

            json.dump(installed,file)
