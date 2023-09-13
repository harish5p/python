from tkinter import *

root = Tk()

text = Text(root)
text.pack()

text.insert('1.0', 'Hello, ')

text.insert('end', 'world!')

text.delete('1.0')
text.delete('end - 2c')

root.mainloop()
