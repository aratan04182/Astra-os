import tkinter as tk

from ui.icons import apps

class Home:

    def __init__(self, root):

        frame = tk.Frame(root)

        frame.pack(expand=True)

        row = 0
        col = 0

        for icon,name in apps:

            button = tk.Button(

                frame,

                text=f"{icon}\n{name}",

                width=10,

                height=4

            )

            button.grid(

                row=row,

                column=col,

                padx=20,

                pady=20

            )

            col += 1

            if col == 3:

                row += 1

                col = 0
