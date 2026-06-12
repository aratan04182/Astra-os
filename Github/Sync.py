import subprocess

def update():

    subprocess.run(
        ["git", "pull"]
    )
