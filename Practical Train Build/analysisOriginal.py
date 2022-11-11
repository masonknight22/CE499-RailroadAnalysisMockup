from tkinter import *



########################## configure window ##########################
root = Tk()
windowColor = "#F3F3F3"
root.geometry("1080x720")
root.configure(bg = windowColor)
root.title("Input Values for Railroad Bridge Analysis")

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


########################## span information label frame ##########################
spanInfoFrame = LabelFrame(window, text="Span Information", bg=windowColor)
spanInfoFrame.grid(row=0, column=0, padx=40, pady=40, ipadx=10, ipady=10)

# span labels
start = Label(spanInfoFrame, text="Start Span", bg=windowColor)
end = Label(spanInfoFrame, text="End Span", bg=windowColor)
increment = Label(spanInfoFrame, text="Span Increment", bg=windowColor)
type = Label(spanInfoFrame, text="LL Type", bg=windowColor)

spacer = Label(spanInfoFrame, text=" ", bg=windowColor)
locations = Label(spanInfoFrame, text="Moment/Stress Calculation Interval Locations", bg=windowColor)
startLoc = Label(spanInfoFrame, text="Start Location", bg=windowColor)
endLoc = Label(spanInfoFrame, text="End Location", bg=windowColor)
interval = Label(spanInfoFrame, text="Interval", bg=windowColor)
step = Label(spanInfoFrame, text="Step Size", bg=windowColor)

# place labels in grid
start.grid(row=0, column=0)
end.grid(row=1, column=0)
increment.grid(row=2, column=0)
type.grid(row=3, column=0)

spacer.grid(row=4, column=0)
locations.grid(row=5, column=0)

startLoc.grid(row=6, column=0)
endLoc.grid(row=7, column=0)
interval.grid(row=8, column=0)
step.grid(row=9, column=0)


# span entries and optionMenu
startEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
startEntry.configure(highlightbackground="black", highlightcolor="black")

endEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
endEntry.configure(highlightbackground="black", highlightcolor="black")

incrementEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
incrementEntry.configure(highlightbackground="black", highlightcolor="black")

llTypeOptionList = ["Custom"]
llTypeText = StringVar()
llTypeText.set(llTypeOptionList[0])
llTypeOptionMenu = OptionMenu(spanInfoFrame, llTypeText, *llTypeOptionList)
llTypeOptionMenu.configure(highlightbackground=windowColor)

startLocEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
startLocEntry.configure(highlightbackground="black", highlightcolor="black")

endLocEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
endLocEntry.configure(highlightbackground="black", highlightcolor="black")

intervalEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
intervalEntry.configure(highlightbackground="black", highlightcolor="black")

stepEntry = Entry(spanInfoFrame, highlightthickness=1, width=3, bd=0)
stepEntry.configure(highlightbackground="black", highlightcolor="black")

# place entries and options in grid
startEntry.grid(row=0, column=1)
endEntry.grid(row=1, column=1)
incrementEntry.grid(row=2, column=1)
llTypeOptionMenu.grid(row=3, column=1)

startLocEntry.grid(row=6, column=1)
endLocEntry.grid(row=7, column=1)
intervalEntry.grid(row=8, column=1)
stepEntry.grid(row=9, column=1)



########################## impact value label frame ##########################
impactFrame = LabelFrame(window, text="Impact Value", bg=windowColor)
impactFrame.grid(row=0, column=1, padx=40, pady=40, ipadx=5, ipady=5)

# create label and place it impact frame grid
impactLabel = Label(impactFrame, text="Design Impact and Year", bg=windowColor)
impactLabel.grid(row=0, column=0)

# impact option menu
impactOptionList = ["Unknown"]
impactText = StringVar()
impactText.set(impactOptionList[0])
impactOptionMenu = OptionMenu(impactFrame, impactText, *impactOptionList)
impactOptionMenu.configure(highlightbackground=windowColor)
impactOptionMenu.grid(row=0, column=1)



########################## output location label frame ##########################
outputFrame = LabelFrame(window, text="Output Location", bg=windowColor)
outputFrame.grid(row=1, column=0, padx=40, pady=40, ipadx=5, ipady=5)

# create label and place it output frame grid
outputLabel = Label(outputFrame, text="Output Location", bg=windowColor)
outputLabel.grid(row=0, column=0)

# output entry
outputEntry = Entry(outputFrame, highlightthickness=1, width=30, bd=0)
outputEntry.configure(highlightbackground="black", highlightcolor="black")
outputEntry.grid(row=0, column=1)



########################## section modulus label frame ##########################
sectionFrame = LabelFrame(window, text="Section Modulus", bg=windowColor)
sectionFrame.grid(row=1, column=1, padx=40, pady=40, ipadx=5, ipady=5)

# section labels
area = Label(sectionFrame, text="Section Area", bg=windowColor)
numGirders = Label(sectionFrame, text="Number of girders", bg=windowColor)
sValue = Label(sectionFrame, text="S Value", bg=windowColor)
hammerBlow = Label(sectionFrame, text="HammerBlow", bg=windowColor)

# add section labels to grid
area.grid(row=0, column=0)
numGirders.grid(row=1, column=0)
sValue.grid(row=2, column=0)
hammerBlow.grid(row=3, column=0)

# section checkboxes and entries
areaCheckValue = IntVar()
areaCheck = Checkbutton(
    sectionFrame,
    text = "Check = Gross, Unchecked = Net",
    variable = areaCheckValue,
    onvalue = 1,
    offvalue = 0,
    bg = windowColor
)

numGirdersEntry = Entry(sectionFrame, highlightthickness=1, width=4, bd=0)
numGirdersEntry.configure(highlightbackground="black", highlightcolor="black")

sValueEntry = Entry(sectionFrame, highlightthickness=1, width=10, bd=0)
sValueEntry.configure(highlightbackground="black", highlightcolor="black")

hammerBlowCheckValue = IntVar()
hammerBlowCheck = Checkbutton(
    sectionFrame,
    text = "Check = Yes, Unchecked = No",
    variable = hammerBlowCheckValue,
    onvalue = 1,
    offvalue = 0,
    bg = windowColor
)

# add section checkboxes and entries to grid
areaCheck.grid(row=0, column=1)
numGirdersEntry.grid(row=1, column=1)
sValueEntry.grid(row=2, column=1)
hammerBlowCheck.grid(row=3, column=1)



########################## dead loads label frame ##########################
deadLoadFrame = LabelFrame(window, text="Dead Loads", bg=windowColor)
deadLoadFrame.grid(row=2, column=0, padx=40, pady=40, ipadx=5, ipady=5)

# deadLoad labels
girderTypeLabel = Label(deadLoadFrame, text="Girder Type", bg=windowColor)
deckTypeLabel = Label(deadLoadFrame, text="Deck Type", bg=windowColor)

girderTypeLabel.grid(row=0, column=0)
deckTypeLabel.grid(row=1, column=0)

# girder type option menu
girderOptionList = ["Deck Plate Girder"]
girderText = StringVar()
girderText.set(girderOptionList[0])
girderOptionMenu = OptionMenu(deadLoadFrame, girderText, *girderOptionList)
girderOptionMenu.configure(highlightbackground=windowColor)
girderOptionMenu.grid(row=0, column=1)

# deck type option menu
deckOptionList = ["Open Timber Deck"]
deckText = StringVar()
deckText.set(deckOptionList[0])
deckOptionMenu = OptionMenu(deadLoadFrame, deckText, *deckOptionList)
deckOptionMenu.configure(highlightbackground=windowColor)
deckOptionMenu.grid(row=1, column=1)



########################## fatigue label frame ##########################
fatigueFrame = LabelFrame(window, text="Dead Loads", bg=windowColor)
fatigueFrame.grid(row=2, column=1, padx=40, pady=40, ipadx=5, ipady=5)

# fatigue labels
impactLoadLabel = Label(fatigueFrame, text="Mean Impact Load", bg=windowColor)
fatigueCategoryLabel = Label(fatigueFrame, text="Fatigue Category", bg=windowColor)
ignoreStressLabel = Label(fatigueFrame, text = "Ignore Stress", bg=windowColor)

impactLoadLabel.grid(row=0, column=0)
fatigueCategoryLabel.grid(row=1, column=0)
ignoreStressLabel.grid(row=2, column=0)

# impact load option menu
impactLoadOptionList = ["Full Design Impact"]
impactLoadText = StringVar()
impactLoadText.set(impactLoadOptionList[0])
impactLoadOptionMenu = OptionMenu(fatigueFrame, impactLoadText, *impactLoadOptionList)
impactLoadOptionMenu.configure(highlightbackground=windowColor)
impactLoadOptionMenu.grid(row=0, column=1)

# fatigue category option menu
fatigueCategoryOptionList = ["A"]
fatigueCategoryText = StringVar()
fatigueCategoryText.set(fatigueCategoryOptionList[0])
fatigueCategoryOptionMenu = OptionMenu(fatigueFrame, fatigueCategoryText, *fatigueCategoryOptionList)
fatigueCategoryOptionMenu.configure(highlightbackground=windowColor)
fatigueCategoryOptionMenu.grid(row=1, column=1)

ignoreStressEntry = Entry(fatigueFrame, highlightthickness=1, width=5, bd=0)
ignoreStressEntry.configure(highlightbackground="black", highlightcolor="black")
ignoreStressEntry.grid(row=2, column=1)



########################## cooper loads label frame ##########################
cooperLoadFrame = LabelFrame(window, text="Dead Loads", bg=windowColor)
cooperLoadFrame.grid(row=3, column=0, padx=40, pady=40, ipadx=5, ipady=5)

# cooper load labels
cooperTypeLabel = Label(cooperLoadFrame, text="Cooper Type", bg=windowColor)
cooperYearLabel = Label(cooperLoadFrame, text="Cooper Year", bg=windowColor)
girderConnectionLabel = Label(cooperLoadFrame, text="Girder Connection", bg=windowColor)

cooperTypeLabel.grid(row=0, column=0)
cooperYearLabel.grid(row=1, column=0)
girderConnectionLabel.grid(row=2, column=0)


# girder type option menu
cooperTypeOptionList = ["40"]
cooperTypeText = StringVar()
cooperTypeText.set(cooperTypeOptionList[0])
cooperTypeOptionMenu = OptionMenu(cooperLoadFrame, cooperTypeText, *cooperTypeOptionList)
cooperTypeOptionMenu.configure(highlightbackground=windowColor)
cooperTypeOptionMenu.grid(row=0, column=1)

# cooper year option menu
cooperYearOptionList = ["1968"]
cooperYearText = StringVar()
cooperYearText.set(cooperYearOptionList[0])
cooperYearOptionMenu = OptionMenu(cooperLoadFrame, cooperYearText, *cooperYearOptionList)
cooperYearOptionMenu.configure(highlightbackground=windowColor)
cooperYearOptionMenu.grid(row=1, column=1)

# deck type option menu
girderConnectionOptionList = ["Welded"]
girderConnectionText = StringVar()
girderConnectionText.set(girderConnectionOptionList[0])
girderConnectionOptionMenu = OptionMenu(cooperLoadFrame, girderConnectionText, *girderConnectionOptionList)
girderConnectionOptionMenu.configure(highlightbackground=windowColor)
girderConnectionOptionMenu.grid(row=2, column=1)



########################## chosen train label frame ##########################
trainFrame = LabelFrame(window, text="Choose Train", bg=windowColor)
trainFrame.grid(row=3, column=1, padx=40, pady=40, ipadx=10, ipady=10)

# train labels
trainPerDayLabel = Label(trainFrame, text="Trains per day", bg=windowColor)
trainSpeedLabel = Label(trainFrame, text="Train Speed", bg=windowColor)
nameLabel = Label(trainFrame, text="Chosen Train Name", bg=windowColor)

trainPerDayLabel.grid(row=0, column=0)
trainSpeedLabel.grid(row=1, column=0)
nameLabel.grid(row=3, column=0)

# train entries and buttons
trainsPerDayEntry = Entry(trainFrame, highlightthickness=1, width=3, bd=0)
trainsPerDayEntry.configure(highlightbackground="black", highlightcolor="black")
trainsPerDayEntry.grid(row=0, column=1)

trainSpeedEntry = Entry(trainFrame, highlightthickness=1, width=3, bd=0)
trainSpeedEntry.configure(highlightbackground="black", highlightcolor="black")
trainSpeedEntry.grid(row=1, column=1)

buildButton = Button(
    trainFrame,
    text="Build Train",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("build train clicked"),
    relief="flat"
)
buildButton.configure(highlightbackground=windowColor)
buildButton.grid(row=2, column=0)

browseButton = Button(
    trainFrame,
    text="Browse",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("browse clicked"),
    relief="flat"
)
browseButton.configure(highlightbackground=windowColor)
browseButton.grid(row=4, column=0)



########################## save label frame ##########################
saveFrame = LabelFrame(window, text="Save All", bg=windowColor)
saveFrame.grid(row=4, column=1, padx=40, pady=40, ipadx=10, ipady=5)

# save button
browseButton = Button(
    saveFrame,
    text="Save",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("save clicked"),
    relief="flat"
)
browseButton.configure(highlightbackground=windowColor)
browseButton.pack(pady=5)



########################## finish label frame ##########################
finishFrame = LabelFrame(window, text="Finish", bg=windowColor)
finishFrame.grid(row=5, column=1, padx=40, pady=40, ipadx=10, ipady=5)

# save button
runButton = Button(
    finishFrame,
    text="Run Program",
    borderwidth=0,
    highlightthickness=1,
    command=lambda: print("run clicked"),
    relief="flat"
)
runButton.configure(highlightbackground=windowColor)
runButton.pack(pady=5)



##########################  tk mainloop ##########################
root.resizable(True, True)
root.mainloop()
