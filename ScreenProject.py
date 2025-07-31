import os

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")
mainWindow["padx"] = 8

lable = tkinter.Label(mainWindow, text="Tkiner Grid Demo")
lable.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, rowspan=2, sticky="nsew")
fileList.config(border=2, relief="sunken")

system32_path = os.path.join(os.environ['WINDIR'], 'System32')
for zone in os.listdir(system32_path):
    fileList.insert(tkinter.END, zone)

listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, rowspan=2, sticky="nsw")
fileList["yscrollcommand"] = listScroll.set

#frame for the radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky="ne")

rbValue = tkinter.IntVar()
rbValue.set(0)  # Default value for radio buttons

# Radio buttons
radio1 = tkinter.Radiobutton(optionFrame, text="File Name", variable=rbValue, value=1)
radio1.grid(row=0, column=0, sticky="w")
radio2 = tkinter.Radiobutton(optionFrame, text="Path", variable=rbValue, value=2)
radio2.grid(row=1, column=0, sticky="w")
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", variable=rbValue, value=3)
radio3.grid(row=2, column=0, sticky="w")

resultLabel = tkinter.Label(mainWindow, text="Result will be shown here")
resultLabel.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky="sw")

# Frame for the time spinner
timeFrame = tkinter.LabelFrame(mainWindow, text="Time")
timeFrame.grid(row=3, column=0, sticky="new")
# Time spinner
hourSpinner = tkinter.Spinbox(timeFrame, from_=0, to=23, width=5)
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=":").grid(row=0, column=1)
minuteSpinner = tkinter.Spinbox(timeFrame, from_=0, to=59, width=5)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=":").grid(row=0, column=3)
secondSpinner = tkinter.Spinbox(timeFrame, from_=0, to=59, width=5)
secondSpinner.grid(row=0, column=4)
timeFrame["padx"] = 36

# Frame for the date spinner
dateFrame = tkinter.Label(mainWindow)
dateFrame.grid(row=4, column=0, sticky="new")

# Date Labels
dayLabel = tkinter.Label(dateFrame, text="Day")
dayLabel.grid(row=0, column=0, sticky="w")
monthLabel = tkinter.Label(dateFrame, text="Month")
monthLabel.grid(row=0, column=1, sticky="w")
yearLabel = tkinter.Label(dateFrame, text="Year")
yearLabel.grid(row=0, column=2, sticky="w")

# Date spinners
daySpinner = tkinter.Spinbox(dateFrame, from_=1, to=31, width=5)
daySpinner.grid(row=1, column=0)
monthSpinner = tkinter.Spinbox(dateFrame, width=5, values=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
monthSpinner.grid(row=1, column=1)
yearSpinner = tkinter.Spinbox(dateFrame, from_=1900, to=2100, width=5)
yearSpinner.grid(row=1, column=2)

# Buttons
okButton = tkinter.Button(mainWindow, text="OK")
okButton.grid(row=4, column=3, sticky="e")
cancelButton = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.quit)
cancelButton.grid(row=4, column=4, sticky="w")

mainWindow.mainloop()

print(rbValue.get())