import tkinter as tk

from ui.home import Home

from ui.dock import Dock

from ui.statusbar import StatusBar

from config import WIDTH,HEIGHT

class Launcher:

    def start(self):

        root = tk.Tk()

        root.geometry(

            f"{WIDTH}x{HEIGHT}"

        )

        root.title("AstraAI OS")

        StatusBar(root)

        Home(root)

        Dock(root)

        root.mainloop()
