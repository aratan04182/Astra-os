import tkinter as tk

from ui.page import PAGE1

class Home:

    def __init__(self, root):

        frame = tk.Frame(root)

        frame.pack(expand=True)

        row = 0

        col = 0

        for icon,name in PAGE1:

            button = tk.Button(

                frame,

                text=f"{icon}\n{name}",

                width=12,

                height=5

            )

            button.grid(

                row=row,

                column=col,

                padx=20,

                pady=20

            )

            col += 1

            if col == 4:

                col = 0

                row += 1
