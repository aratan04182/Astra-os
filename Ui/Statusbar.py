import tkinter as tk
import time

class StatusBar:

    def __init__(self, root):

        self.label = tk.Label(
            root,
            text="",
            anchor="e"
        )

        self.label.pack(fill="x")

        self.update()

    def update(self):

        now = time.strftime("%H:%M")

        self.label.config(
            text=f"WiFi   🔋100%   {now}"
        )

        self.label.after(1000, self.update)
