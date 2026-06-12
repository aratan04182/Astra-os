import time
from ai.brain import Brain

def start():

    print("================================")
    print(" AstraAI Booting...")
    print("================================")

    brain = Brain()

    while True:

        brain.run()

        time.sleep(1)
