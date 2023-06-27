from tkinter import*

root = Tk()

w = 1000
h = 500
ws = root.winfo_screenwidth()
wh = root.winfo_screenheight()

x = ws - 1000
y = 0

root.geometry("{0}x{1}+{2}+{3}".format(w, h, x, y))

root.mainloop()