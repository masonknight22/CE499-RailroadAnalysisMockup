from tkinter import *



# configure window
window = Tk()
windowColor = "#F2F2F2"
window.geometry("600x800")
window.configure(bg = windowColor)
window.title("Train Build")

# make canvas and window scrollable
window.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

# train car frame
frameb = LabelFrame(
    window,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
frameb.place(
    x=56,
    y=48,
    width=487,
    height=155
)
canvas = Canvas(frameb, bg="#FFFFFF", highlightthickness=0, width=592, height=278)
canvas.pack(expand=True,side=LEFT,fill=BOTH)
carFrame = Frame(canvas, bg=windowColor, highlightthickness=0, bd = 0)
carFrame.pack()

# column labels
typeTrain = Label(window, text="Train Build", bg="#FFFFFF", font='Helvetica 22 bold')
typeTrain.place(x = 72, y = 64)

# train name entry and label
trainNameEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
trainNameEntry.configure(highlightbackground="black", highlightcolor="black")
trainNameEntry.place(
    x=74,
    y=135,
    width=335,
    height=22
)
trainNameLabel = Label(window, text="Train Name", bg="#FFFFFF")
trainNameLabel.place(x = 73, y = 108)

# total cars entry and label
totalCarsEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
totalCarsEntry.configure(highlightbackground="black", highlightcolor="black")
totalCarsEntry.place(
    x=428,
    y=135,
    width=90,
    height=22
)
totalCarsLabel = Label(window, text="Number of Cars", bg="#FFFFFF")
totalCarsLabel.place(x = 426, y = 108)



# train car frame
frame = LabelFrame(
    window,
    bg="#FFFFFF", #optional background color
    bd=0,
    highlightthickness=0

)
frame.place(
    x=56,
    y=233,
    width=487,
    height=519
)
canvas = Canvas(frame, bg="#FFFFFF", bd=0, highlightthickness=0, width=592, height=278)
canvas.pack(expand=True,side=LEFT,fill=BOTH)
carFrame = Frame(canvas, bg="#FFFFFF")
carFrame.pack()

# column labels
typeCars = Label(window, text="Train Cars", bg="#FFFFFF", font='Helvetica 22 bold')
typeCars.place(x = 72, y = 249)

# column labels
typeCarLabel = Label(carFrame, text="Type of Car", bg="#FFFFFF", font='Helvetica 12 bold')
numCarsLabel = Label(carFrame, text="Number of Cars", bg="#FFFFFF", font='Helvetica 12 bold')
weightLabel = Label(carFrame, text="Weight of Car %", bg="#FFFFFF", font='Helvetica 12 bold')
typeCarLabelSpace = Label(carFrame, text="", bg="#FFFFFF", font='Helvetica 12 bold')

typeCarLabelSpace.grid(row=0, column=0, padx=25, pady=20)
typeCarLabel.grid(row=1,column=0, padx=25, pady=10)
numCarsLabel.grid(row=1, column=1, padx=25, pady=10)
weightLabel.grid(row=1, column=2, padx=25, pady=10)

# default row
locomotive = Label(carFrame, text="Locomotive", bg="#FFFFFF")
locomotive.place(x = 68, y = 300)
numCarsEntry = Entry(carFrame, highlightthickness=0, width=3, bd=0, bg="#E6E6E6")
numCarsEntry.configure(highlightbackground="black", highlightcolor="black")
weightScale = Scale(carFrame, bg="#FFFFFF", orient="horizontal")

locomotive.grid(row=2,column=0, padx=25)
numCarsEntry.grid(row=2, column=1, padx=25)
weightScale.grid(row=2, column=2, padx=25)

# list of options for type of car
optionList = ["Unit Coal", "Locomotive", "Train Car", "Train Car"]


# remaining rows starting on row 2 (base 0)
# change numRows to set initial number rows
numRows = 9
for r in range(3, numRows):
    c = 0

    text = StringVar()
    text.set(optionList[0])
    option = OptionMenu(carFrame, text, *optionList)
    option.configure(highlightbackground="#FFFFFF")
    entry = Entry(carFrame, highlightthickness=0, width=3, bd=0, bg="#E6E6E6")
    entry.configure(highlightbackground="#FFFFFF", highlightcolor="black")

    scale = Scale(carFrame, bg="#FFFFFF", orient="horizontal")

    option.grid(row=r, column=c, padx=25)
    c += 1
    entry.grid(row=r, column=c, padx=25)
    c += 1
    scale.grid(row=r, column=c, padx=25)



# add car button
addCarButton = Button(
    text="Add Car",
    bg="#E6E6E6",
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("add clicked"),
    relief="flat"
)
addCarButton.configure(highlightbackground="#FFFFFF", bg="#F3F3F3")
addCarButton.place(
    x=100.0,
    y=610.0,
    width=78.0,
    height=20.0
)

# save button
saveButton = Button(
    text="Save",
    borderwidth=0,
    highlightbackground="#0066FF",
    highlightthickness=0,
    command=lambda: print("save clicked"),
    relief="flat"
)
saveButton.configure(highlightbackground="#FFFFFF")
saveButton.place(
    x=437.0,
    y=711.0,
    width=78,
    height=20
)

# close button
closeButton = Button(
    text="Close",
    borderwidth=0,
    bg="#F3F3F3",
    fg="#000000",
    highlightthickness=0,
    command=lambda: print("close clicked"),
    relief="flat"
)
closeButton.configure(highlightbackground="#FFFFFF")
closeButton.place(
    x=347.0,
    y=711.0,
    width=78,
    height=20
)



##########################  tk mainloop ##########################
window.resizable(True, True)
window.mainloop()
