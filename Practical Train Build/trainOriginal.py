from tkinter import *



# configure window
window = Tk()
windowColor = "#F3F3F3"
window.geometry("960x540")
window.configure(bg = windowColor)
window.title("Train Build")



# train name entry and label
trainNameEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=1
)
trainNameEntry.configure(highlightbackground="black", highlightcolor="black")
trainNameEntry.place(
    x=469.0,
    y=27.0,
    width=154.0,
    height=24.0
)
trainNameLabel = Label(window, text="Train Name", bg=windowColor)
trainNameLabel.place(x = 380, y = 28)

# total cars entry and label
totalCarsEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=1
)
totalCarsEntry.configure(highlightbackground="black", highlightcolor="black")
totalCarsEntry.place(
    x=469.0,
    y=66.0,
    width=154.0,
    height=24.0
)
totalCarsLabel = Label(window, text="Total Different Cars", bg=windowColor)
totalCarsLabel.place(x = 335, y = 67)



# train car frame
frame = LabelFrame(
    window,
    text="Train Cars",
    #bg="#D9D9D9" #optional background color
    bg=windowColor
)
frame.place(
    x=184,
    y=131,
    width=592,
    height=278
)
canvas = Canvas(frame, bg=windowColor, bd=0, highlightthickness=0, width=592, height=278)
canvas.pack(expand=True,side=LEFT,fill=BOTH)
carFrame = Frame(canvas, bg=windowColor)
carFrame.pack()



# column labels
typeCarLabel = Label(carFrame, text="TYPE OF CAR", bg=windowColor)
numCarsLabel = Label(carFrame, text="NUMBER OF CARS", bg=windowColor)
weightLabel = Label(carFrame, text="WEIGHT OF CAR (PERCENTAGE)", bg=windowColor)

typeCarLabel.grid(row=0,column=0, padx=25)
numCarsLabel.grid(row=0, column=1, padx=25)
weightLabel.grid(row=0, column=2, padx=25)

# default row
locomotive = Label(carFrame, text="Locomotive", bg=windowColor)
numCarsEntry = Entry(carFrame, highlightthickness=1, width=3, bd=0)
numCarsEntry.configure(highlightbackground="black", highlightcolor="black")
weightScale = Scale(carFrame, bg=windowColor, orient="horizontal")

locomotive.grid(row=1,column=0, padx=25)
numCarsEntry.grid(row=1, column=1, padx=25)
weightScale.grid(row=1, column=2, padx=25)

# list of options for type of car
optionList = ["Unit Coal"]

# remaining rows starting on row 2 (base 0)
# change numRows to set initial number rows
numRows = 7
for r in range(2, numRows):
    c = 0

    text = StringVar()
    text.set(optionList[0])
    option = OptionMenu(carFrame, text, *optionList)
    option.configure(highlightbackground=windowColor)
    entry = Entry(carFrame, highlightthickness=1, width=3, bd=0)
    entry.configure(highlightbackground="black", highlightcolor="black")

    scale = Scale(carFrame, bg=windowColor, orient="horizontal")

    option.grid(row=r, column=c, padx=25)
    c += 1
    entry.grid(row=r, column=c, padx=25)
    c += 1
    scale.grid(row=r, column=c, padx=25)



# add car button
addCarButton = Button(
    text="Add Car",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("add clicked"),
    relief="flat"
)
addCarButton.configure(highlightbackground=windowColor)
addCarButton.place(
    x=650.0,
    y=423.0,
    width=130.0,
    height=20.0
)

# save button
saveButton = Button(
    text="Save Train Set-Up",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("save clicked"),
    relief="flat"
)
saveButton.configure(highlightbackground=windowColor)
saveButton.place(
    x=650.0,
    y=453.0,
    width=130.0,
    height=20.0
)

# close button
closeButton = Button(
    text="Close",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("close clicked"),
    relief="flat"
)
closeButton.configure(highlightbackground=windowColor)
closeButton.place(
    x=650.0,
    y=483.0,
    width=130.0,
    height=20.0
)



##########################  tk mainloop ##########################
window.resizable(True, True)
window.mainloop()
