#hier is de welkelijke tkinter app

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
    ontspanningstool.pack()

def clearFrames():
    rekentool.pack_forget()
    ontspanningstool.pack_forget()
    opdr3.pack_forget()

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
menubar.add_cascade(label="Tool", menu=mainmenu)


#rekentool
rekentool = Frame(borderwidth=10)
label_1 = Label(rekentool, text="REKENTOOL", bg = "blue", fg="white", width=20, height=8)
label_1.pack()

#ontspanningstool
ontspanningstool = Frame(borderwidth=10)
label_1 = Label(ontspanningstool, text="ONSTPANNINGSTOOL", bg = "purple", fg="white", width=20, height=8)
label_1.pack()

#opdracht 3
opdr3 = Frame(borderwidth=10)
label_1 = Label(opdr3, text="OPDRACHT 3", bg = "red", fg="white", width=20, height=8)
label_1.pack()








window.mainloop()