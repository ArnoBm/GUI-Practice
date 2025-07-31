try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

mainWindow = tkinter.Tk()

mainWindow.title("Hello World")
mainWindow.geometry("640x480+8+200")

label = tkinter.Label(mainWindow, text="Hi! This Arnob Mustakim")
label.pack(side="top")

leftFrame = tkinter.Frame(mainWindow)
leftFrame.pack(side="left", anchor="n", fill=tkinter.Y, expand=False)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.pack(side="left", anchor="n")

rightFrame = tkinter.Frame(mainWindow)
rightFrame.pack(side="right", anchor="n", expand=True)

button1 = tkinter.Button(rightFrame, text="Button 1")
button1.pack(side="top", anchor="n")
button2 = tkinter.Button(rightFrame, text="Button 2")
button2.pack(side="top", anchor="s")
button3 = tkinter.Button(rightFrame, text="Button 3")
button3.pack(side="top", anchor="e")

mainWindow.mainloop()