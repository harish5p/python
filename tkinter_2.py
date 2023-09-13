from tkinter import *

root = Tk()

v = StringVar()

rb1 = Radiobutton(root, text="Option 1", variable=v, value="1")
rb2 = Radiobutton(root, text="Option 2", variable=v, value="2")
rb3 = Radiobutton(root, text="Option 3", variable=v, value="3")

rb1.pack()
rb2.pack()
rb3.pack()

root.mainloop()
