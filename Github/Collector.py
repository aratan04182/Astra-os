import os
import subprocess

class Collector:

    def clone(self, url):

        name = url.split("/")[-1].replace(".git", "")

        path = "repositories/" + name

        if os.path.exists(path):
            return path

        subprocess.run([
            "git",
            "clone",
            url,
            path
        ])

        return path
