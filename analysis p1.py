import tkinter
from tkinter import *
from PIL import ImageTk, Image



# configure window
root = Tk()
windowColor = "#F2F2F2"
root.geometry("827x1500")
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

image1 = Image.open("Asset 4.png")
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test, width = 753, height = 355, bg=windowColor)
label1.place(x=150, y=25)


# span information frame
framea = LabelFrame(
    root,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
framea.place(
    x=60,
    y=48,
    width=334,
    height=390
)



infoSpan = Label(root, text="Span Information", bg="#FFFFFF", font='Helvetica 22 bold')
infoSpan.place(x = 72, y = 64)

# start span name and label
startSpanEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
startSpanEntry.configure(highlightbackground="black", highlightcolor="black")
startSpanEntry.place(
    x=292,
    y=104,
    width=87,
    height=22
)
startSpanLabel = Label(root, text="Start Span", bg="#FFFFFF")
startSpanLabel.place(x = 100, y = 108)

# end span name and label
endSpanEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
endSpanEntry.configure(highlightbackground="black", highlightcolor="black")
endSpanEntry.place(
    x=292,
    y=139,
    width=87,
    height=22
)
endSpanLabel = Label(root, text="End Span", bg="#FFFFFF")
endSpanLabel.place(x = 100, y = 142)

# span increment name and label
incrementSpanEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
incrementSpanEntry.configure(highlightbackground="black", highlightcolor="black")
incrementSpanEntry.place(
    x=292,
    y=174,
    width=87,
    height=22
)
incrementSpanLabel = Label(root, text="Span Increment", bg="#FFFFFF")
incrementSpanLabel.place(x = 100, y = 178)


llTypeOptionList = ["Custom", "Option", "Option", "Option"]

lltext = StringVar()
lltext.set(llTypeOptionList[0])
lloption = OptionMenu(root, lltext, *llTypeOptionList)
lloption.configure(highlightbackground="#FFFFFF")
lloption.place(x = 279, y = 215)

llTypeLabel = Label(root, text="LL Type", bg="#FFFFFF")
llTypeLabel.place(x = 100, y = 213)

infoSpan = Label(root, text="Moment/Stress Calculation Interval Locations", bg="#FFFFFF", font='Helvetica 13 bold')
infoSpan.place(x = 77, y = 248)

# start location name and label
startLocationEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
startLocationEntry.configure(highlightbackground="black", highlightcolor="black")
startLocationEntry.place(
    x=292,
    y=279,
    width=87,
    height=22
)
startLocationLabel = Label(root, text="Start Location", bg="#FFFFFF")
startLocationLabel.place(x = 100, y = 283)

# end location name and label
endLocationEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
endLocationEntry.configure(highlightbackground="black", highlightcolor="black")
endLocationEntry.place(
    x=292,
    y=314,
    width=87,
    height=22
)
endLocationLabel = Label(root, text="End Location", bg="#FFFFFF")
endLocationLabel.place(x = 100, y = 318)

# interval name and label
intervalEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
intervalEntry.configure(highlightbackground="black", highlightcolor="black")
intervalEntry.place(
    x=292,
    y=349,
    width=87,
    height=22
)
intervalLabel = Label(root, text="Interval", bg="#FFFFFF")
intervalLabel.place(x = 100, y = 353)

# step size name and label
stepSizeEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
stepSizeEntry.configure(highlightbackground="black", highlightcolor="black")
stepSizeEntry.place(
    x=292,
    y=384,
    width=87,
    height=22
)
stepSizeLabel = Label(root, text="Step Size", bg="#FFFFFF")
stepSizeLabel.place(x = 100, y = 388)

# loads frame
framec = LabelFrame(
    root,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
framec.place(
    x=60,
    y=473,
    width=334,
    height=286
)



loadsDead = Label(root, text="Dead Loads", bg="#FFFFFF", font='Helvetica 22 bold')
loadsDead.place(x = 75, y = 489)

# girder type name and label


girderTypeOptionList = ["Custom", "Option", "Option", "Option"]

girdertext = StringVar()
girdertext.set(girderTypeOptionList[0])
girderoption = OptionMenu(root, girdertext, *girderTypeOptionList)
girderoption.configure(highlightbackground="#FFFFFF")
girderoption.place(x = 292, y = 529)

typeGirderLabel = Label(root, text="Girder Type", bg="#FFFFFF")
typeGirderLabel.place(x = 100, y = 533)

# deck type name and label
deckTypeOptionList = ["Custom", "Option", "Option", "Option"]

decktext = StringVar()
decktext.set(deckTypeOptionList[0])
deckoption = OptionMenu(root, decktext, *deckTypeOptionList)
deckoption.configure(highlightbackground="#FFFFFF")
deckoption.place(x = 292, y = 564)

typeDeckLabel = Label(root, text="Deck Type", bg="#FFFFFF")
typeDeckLabel.place(x = 100, y = 568)

loadsDead = Label(root, text="Cooper Loads", bg="#FFFFFF", font='Helvetica 22 bold')
loadsDead.place(x = 75, y = 597)

# cooper type name and label

cooperTypeOptionList = ["Custom", "Option", "Option", "Option"]

coopertext = StringVar()
coopertext.set(cooperTypeOptionList[0])
cooperoption = OptionMenu(root, coopertext, *cooperTypeOptionList)
cooperoption.configure(highlightbackground="#FFFFFF")
cooperoption.place(x = 292, y = 635)

typeCooperLabel = Label(root, text="Cooper Type", bg="#FFFFFF")
typeCooperLabel.place(x = 100, y = 639)

# cooper year name and label
cooperYearTypeOptionList = ["Custom", "Option", "Option", "Option"]

cooperYeartext = StringVar()
cooperYeartext.set(cooperYearTypeOptionList[0])
cooperYearoption = OptionMenu(root, cooperYeartext, *cooperYearTypeOptionList)
cooperYearoption.configure(highlightbackground="#FFFFFF")
cooperYearoption.place(x = 292, y = 670)

yearCooperLabel = Label(root, text="Cooper Year", bg="#FFFFFF")
yearCooperLabel.place(x = 100, y = 674)

# girder connection name and label
girderTypeOptionList = ["Custom", "Option", "Option", "Option"]

girdertext = StringVar()
girdertext.set(girderTypeOptionList[0])
girderoption = OptionMenu(root, girdertext, *girderTypeOptionList)
girderoption.configure(highlightbackground="#FFFFFF")
girderoption.place(x = 292, y = 705)

connectionGirderLabel = Label(root, text="Girder Connection", bg="#FFFFFF")
connectionGirderLabel.place(x = 100, y = 709)



valueImpact = Label(root, text="Impact Value", bg=windowColor, font='Helvetica 22 bold')
valueImpact.place(x = 448, y = 64)


# impact option and bridge
impactTypeOptionList = ["Unknown", "Option", "Option", "Option"]

impacttext = StringVar()
impacttext.set(impactTypeOptionList[0])
impactoption = OptionMenu(root, impacttext, *impactTypeOptionList)
impactoption.configure(highlightbackground="#FFFFFF")
impactoption.place(x = 633, y = 103)

impactTypeLabel = Label(root, text="Design Impact and Year", bg=windowColor)
impactTypeLabel.place(x = 474, y = 104)



# section modulus frame
frameb = LabelFrame(
    root,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
frameb.place(
    x=433,
    y=282,
    width=334,
    height=477
)






# column labels
modulusSection = Label(root, text="Section Modulus", bg="#FFFFFF", font='Helvetica 22 bold')
modulusSection.place(x = 448, y = 300)


# section area load name and label
areaCheck1Value = IntVar()
areaCheck1 = Checkbutton(
    root,
    text = "Gross",
    variable = areaCheck1Value,
    onvalue = 1,
    offvalue = 0,
    bg = "#ffffff"
)
areaCheck1.place(
    x = 665,
    y = 341
)
areaCheck2Value = IntVar()
areaCheck2 = Checkbutton(
    root,
    text = "Net",
    variable = areaCheck2Value,
    onvalue = 1,
    offvalue = 0,
    bg = "#ffffff"
)
areaCheck2.place(
    x = 665,
    y = 368
)

areaSectionLabel = Label(root, text="Section Area", bg="#FFFFFF")
areaSectionLabel.place(x = 473, y = 340)

# number of girders name and label
girderSectionEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
girderSectionEntry.configure(highlightbackground="black", highlightcolor="black")
girderSectionEntry.place(
    x=665,
    y=406,
    width=87,
    height=22
)
girderSectionLabel = Label(root, text="Number of Girders", bg="#FFFFFF")
girderSectionLabel.place(x = 473, y = 410)

# S value name and label
sValueEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
sValueEntry.configure(highlightbackground="black", highlightcolor="black")
sValueEntry.place(
    x=665,
    y=445,
    width=87,
    height=22
)
sValueLabel = Label(root, text="S Value", bg="#FFFFFF")
sValueLabel.place(x = 473, y = 449)


# Hammer Blow name and label
blowCheck1Value = IntVar()
blowCheck1 = Checkbutton(
    root,
    text = "Yes",
    variable = blowCheck1Value,
    onvalue = 1,
    offvalue = 0,
    bg = "#ffffff"
)
blowCheck1.place(
    x = 665,
    y = 489
)
blowCheck2Value = IntVar()
blowCheck2 = Checkbutton(
    root,
    text = "No",
    variable = blowCheck2Value,
    onvalue = 1,
    offvalue = 0,
    bg = "#ffffff"
)
blowCheck2.place(
    x = 665,
    y = 516
)

blowHammerLabel = Label(root, text="Hammer Blow", bg="#FFFFFF")
blowHammerLabel.place(x = 473, y = 488)



modulusSection = Label(root, text="Fatigue", bg="#FFFFFF", font='Helvetica 22 bold')
modulusSection.place(x = 448, y = 547)


# mean impact load name and label
impactTypeOptionList = ["Custom", "Option", "Option", "Option"]

impacttext = StringVar()
impacttext.set(impactTypeOptionList[0])
impactoption = OptionMenu(root, impacttext, *impactTypeOptionList)
impactoption.configure(highlightbackground="#FFFFFF")
impactoption.place(x = 665, y = 587)

meanImpactLoadLabel = Label(root, text="Mean Impact Load", bg="#FFFFFF")
meanImpactLoadLabel.place(x = 473, y = 591)

# fatigue category name and label
fatigueTypeOptionList = ["Custom", "Option", "Option", "Option"]

fatiguetext = StringVar()
fatiguetext.set(fatigueTypeOptionList[0])
fatigueoption = OptionMenu(root, fatiguetext, *fatigueTypeOptionList)
fatigueoption.configure(highlightbackground="#FFFFFF")
fatigueoption.place(x = 665, y = 622)

categoryFatigueLabel = Label(root, text="Fatigue Category", bg="#FFFFFF")
categoryFatigueLabel.place(x = 473, y = 626)

# ignore stress name and label
ignoreStressEntry = Entry(
    bd=0,
    bg="#E6E6E6",
    fg="#000716",
    highlightthickness=0
)
ignoreStressEntry.configure(highlightbackground="black", highlightcolor="black")
ignoreStressEntry.place(
    x=665,
    y=657,
    width=87,
    height=22
)
ignoreStressLabel = Label(root, text="Ignore Stress", bg="#FFFFFF")
ignoreStressLabel.place(x = 473, y = 661)




#####################################################

# train frame
framet = LabelFrame(
    root,
    bg="#FFFFFF", 
    bd=0,
    highlightthickness=0
    
)
framet.place(
    x=60,
    y=794,
    width=707,
    height=211
)



chooseTrain = Label(root, text="Choose Train", bg="#FFFFFF", font='Helvetica 22 bold')
chooseTrain.place(x = 92, y = 810)





#####################################################

# save button


# close button




##########################  tk mainloop ##########################
root.resizable(True, True)
root.mainloop()
