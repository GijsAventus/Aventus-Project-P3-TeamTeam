#hier is de welkelijke tkinter app

#imports
from asyncio.windows_events import NULL
import classes
from tkinter import *


#functies

def showRekentool():
    clearFrames()
    rekentool.pack()

def showOntspanningstool():
    clearFrames()
    ontspanningstool.pack()

def showOpdr3():
    clearFrames()
    opdr3.pack()

def clearFrames():
    rekentool.pack_forget()
    ontspanningstool.pack_forget()
    opdr3.pack_forget()

def calcBtw():
    global rkConsole
    btw = rkBtwInput.get("1.0", END)
    rkColsole.insert(END, f"De te betalen BTW is {classes.calculate.btw(btw)}")

def calcReistijd():
    rkRstInput1.get("1.0", END)
    rkRstInput2.get("1.0", END)

#window
window = Tk()
window.title("Programmeren P3 Eindopdracht")

#menu aanmaken
menubar = Menu(window)
window.config(menu=menubar)

#menu items aanmaken
mainmenu = Menu(menubar)
mainmenu.add_command(label="Rekentool", command=showRekentool)        
mainmenu.add_command(label="Ontspanningstool", command=showOntspanningstool)        
mainmenu.add_command(label="Opdracht 3", command=showOpdr3)        
mainmenu.add_command(label="Clear", command=clearFrames)        
mainmenu.add_separator()
mainmenu.add_command(label="Exit", command=window.quit)
#menubar toevoegen
menubar.add_cascade(label="Scherm", menu=mainmenu)



#rekentool
rekentool = Frame(borderwidth=10)
rkConsole = Text(rekentool, width=70, height=8)
rkConsole.grid(row=0, column=0, columnspan=10)

#btw calculator
rkBtwLabel = Label(rekentool, text="Bereken te betalen btw")
rkBtwLabel.grid(row=1, column=0, sticky=W)

rkBtwInputLabel = Label(rekentool, text="Vul een getal in:")
rkBtwInputLabel.grid(row=2, column=0, sticky=W)

rkBtwInput = Text(rekentool, width=15, height=1)
rkBtwInput.grid(row=3,column=0, sticky=W)

rkBtwSubmit = Button(rekentool, text="Bevestigen", command=calcBtw())


#reistijd calculator
rkRstLabel = 0

rkRstInputLabel = 0

rkRstInput1 = Text(rekentool, width=10, height=1)

rkRstInput2 = Text(rekentool, width=10, height=1)

rkRstSubmit = 0



#ontspanningstool
ontspanningstool = Frame(borderwidth=10)
label_1 = Label(ontspanningstool, text="ONSTPANNINGSTOOL", bg = "purple", fg="white", width=20, height=8)
label_1.pack()


#opdracht 3
opdr3 = Frame(borderwidth=10)
label_1 = Label(opdr3, text="OPDRACHT 3", bg = "red", fg="white", width=20, height=8)
label_1.pack()








window.mainloop()