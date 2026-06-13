import tkinter as tk

class Dock:

    def __init__(self, root):

        frame = tk.Frame(root)

        frame.pack(side="bottom")

        apps = [

            "🤖",

            "🌍",

            "📂",

            "⚙"

        ]

        for app in apps:

            button = tk.Button(

                frame,

                text=app,

                width=6,

                height=2

            )

            button.pack(side="left", padx=10)
