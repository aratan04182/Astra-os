import tkinter as tk

from ui.home import Home

from ui.statusbar import StatusBar

from config import WIDTH,HEIGHT

class Launcher:

    def start(self):

        root = tk.Tk()

        root.title("AstraAI OS")

        root.geometry(f"{WIDTH}x{HEIGHT}")

        StatusBar(root)

        Home(root)

        root.mainloop()
