import tkinter
from tkinter import *
from PIL import ImageTk, Image



# configure window
root = Tk()
windowColor = "#F2F2F2"
root.geometry("827x700")
root.configure(bg = windowColor)
root.title("Train Build")


# create a container for canvas so window is scrollable
# window is a frame inside canvas that is a container for rest of application
container = Frame(root, bg = windowColor)
canvas = Canvas(container, bg = windowColor, bd=0, highlightthickness=0)
scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
window = Frame(canvas, bg = windowColor)

# make canvas and window scrollable
window.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=window, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


# pack containers into root
container.pack(side="left", fill="both", expand=True)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")





# train frame
framet = LabelFrame(
    root,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
framet.place(
    x=60,
    y=48,
    width=707,
    height=221
)



chooseTrain = Label(root, text="Choose Train", bg="#FFFFFF", font='Helvetica 22 bold')
chooseTrain.place(x = 72, y = 64)






image1 = Image.open("Asset 2.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test, width = 653, height = 77, bg="#ffffff")
label1.place(x=80, y=105)




# end span name and label
dayTrainsEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
dayTrainsEntry.configure(highlightbackground="black", highlightcolor="black")
dayTrainsEntry.place(
    x=292,
    y=190,
    width=87,
    height=22
)
dayTrainsLabel = Label(root, text="Trains per Day", bg="#FFFFFF")
dayTrainsLabel.place(x = 100, y = 192)

# span increment name and label
speedTrainsEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
speedTrainsEntry.configure(highlightbackground="black", highlightcolor="black")
speedTrainsEntry.place(
    x=292,
    y=230,
    width=87,
    height=22
)
speedTrainsLabel = Label(root, text="Train Speed", bg="#FFFFFF")
speedTrainsLabel.place(x = 100, y = 232)


# span increment name and label
outputEntry = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
outputEntry.configure(highlightbackground="black", highlightcolor="black")
outputEntry.place(
    x=217,
    y=304,
    width=290,
    height=22
)
outputLabel = Label(root, text="Output Location", bg=windowColor)
outputLabel.place(x = 100, y = 302)


# save button
browseButton = Button(
    text="Save",
    borderwidth=0,
    highlightbackground="#0066FF",
    highlightthickness=0,
    command=lambda: print("save clicked"),
    relief="flat"
)
browseButton.configure(highlightbackground="#FFFFFF")
browseButton.place(
    x=607.0,
    y=192.0,
    width=78,
    height=20
)

# close button
saveTrainButton = Button(
    text="Browse...",
    borderwidth=0,
    bg="#F3F3F3",
    fg="#000000",
    highlightthickness=0,
    command=lambda: print("close clicked"),
    relief="flat"
)
saveTrainButton.configure(highlightbackground="#FFFFFF")
saveTrainButton.place(
    x=497.0,
    y=192.0,
    width=78,
    height=20
)

#####################################################

# save button
finishButton = Button(
    text="Finish",
    borderwidth=0,
    highlightbackground="#0066FF",
    highlightthickness=0,
    command=lambda: print("save clicked"),
    relief="flat"
)
finishButton.configure(highlightbackground="#FFFFFF")
finishButton.place(
    x=667.0,
    y=302.0,
    width=78,
    height=20
)

# close button
saveButton = Button(
    text="Save All",
    borderwidth=0,
    bg="#F3F3F3",
    fg="#000000",
    highlightthickness=0,
    command=lambda: print("close clicked"),
    relief="flat"
)
saveButton.configure(highlightbackground="#FFFFFF")
saveButton.place(
    x=557.0,
    y=302.0,
    width=78,
    height=20
)

##########################  tk mainloop ##########################
root.resizable(True, True)
root.mainloop()
