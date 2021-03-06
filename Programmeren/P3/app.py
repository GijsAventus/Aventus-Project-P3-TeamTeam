#imports
from classes import *
from tkinter import *
import tkinter.messagebox
import pickle 

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
    inputValue = rkBtwInput.get("1.0", END)
    rkConsole.insert("1.0", f"\n{calculate.btw(inputValue)}\n")

def calcReistijd():
    Afstand = rkRstInputAfstand.get("1.0", END)
    Snelheid = rkRstInputSnelheid.get("1.0", END)
    rkConsole.insert("1.0", f"\n{calculate.reistijd(Afstand, Snelheid)}\n")

def calcVierkant():
    Lengte = rkVktInputLengte.get("1.0", END)
    Breedte = rkVktInputBreedte.get("1.0", END)
    rkConsole.insert("1.0", f"\n{calculate.vierkant(Lengte, Breedte)}\n")

def calcCirkel():
    inputValue = rkCklInput.get("1.0", END)
    rkConsole.insert("1.0", f"\n{calculate.cirkel(inputValue)}\n")

def calcPct():
    input1 = rkPctInput1.get("1.0", END)
    input2 = rkPctInput2.get("1.0", END)
    rkConsole.insert("1.0", f"\n{calculate.procent(input1, input2)}\n")
    
def add_task():
    task = entry_task.get()
    if task !='':
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title='Waarschuwing!', message='Je moet een taak uitvoeren.')

def delete_task():
    try:
        task_index=listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title='Waarschuwing!', message='Je moet een taak selecteren om deze te kunnen verwijderen.')

def load_task():
    try:
       tasks=pickle.load(open('Taak.data', 'rb'))
       listbox_tasks.delete(0, tkinter.END)
       for task in tasks:
           listbox_tasks.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title='Waarschuwing!', message='Kan het bestand niet vinden of ophalen.')



def save_task():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open('Taak.data', 'wb'))

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
rkConsole = Text(rekentool, width=80, height=8)
rkConsole.grid(row=0, column=0, columnspan=15)

#btw calculator
rkBtwLabel = Label(rekentool, text="Te betalen BTW berekenen")
rkBtwLabel.grid(row=1, column=0, sticky=W, columnspan=2)

rkBtwInputLabel = Label(rekentool, text="Vul een bedrag in (Euro):")
rkBtwInputLabel.grid(row=2, column=0, sticky=W, columnspan=2)

rkBtwInput = Text(rekentool, width=10, height=1)
rkBtwInput.grid(row=3,column=0, sticky=W)

rkBtwSubmit = Button(rekentool, text="Bevestigen", command=calcBtw)
rkBtwSubmit.grid(row=4, column=0, sticky=W)

#reistijd calculator
rkRstLabel = Label(rekentool, text="Reistijd berekenen")
rkRstLabel.grid(row=1, column=4, sticky=W, columnspan=2)

rkRstInputLabelAfstand = Label(rekentool, text="Afstand (Meter)")
rkRstInputLabelAfstand.grid(row=2, column=4, sticky=W)

rkRstInputLabelSnelheid = Label(rekentool, text="Snelheid (M/S)")
rkRstInputLabelSnelheid.grid(row=2, column=5, sticky=W)

rkRstInputAfstand = Text(rekentool, width=10, height=1)
rkRstInputAfstand.grid(row=3, column=4, sticky=W)

rkRstInputSnelheid = Text(rekentool, width=10, height=1)
rkRstInputSnelheid.grid(row=3, column=5, sticky=W)

rkRstSubmit = Button(rekentool, text="Bevestigen", command=calcReistijd)
rkRstSubmit.grid(row=4, column=4, sticky=W)

#vierkant calculator
rkVktLabel = Label(rekentool, text="Vierkant berekenen")
rkVktLabel.grid(row=6, column=0, sticky=W, columnspan=2)

rkVktInputLabelLengte = Label(rekentool, text="Lengte (cm)")
rkVktInputLabelLengte.grid(row=7, column=0, sticky=W)

rkVktInputLabelBreedte = Label(rekentool, text="Breedte (cm)")
rkVktInputLabelBreedte.grid(row=7, column=1, sticky=W)

rkVktInputLengte = Text(rekentool, width=10, height=1)
rkVktInputLengte.grid(row=8, column=0, sticky=W)

rkVktInputBreedte = Text(rekentool, width=10, height=1)
rkVktInputBreedte.grid(row=8, column=1, sticky=W)

rkVktSubmit = Button(rekentool, text="Bevestigen", command=calcVierkant)
rkVktSubmit.grid(row=9, column=0, sticky=W)

#cirkel calculator
rkCklLabel = Label(rekentool, text="Cirkel berekenen")
rkCklLabel.grid(row=6, column=4, sticky=W)

rkCklInputLabel = Label(rekentool, text="Diameter (cm)")
rkCklInputLabel.grid(row=7, column=4, sticky=W)

rkCklInput = Text(rekentool, width=10, height=1)
rkCklInput.grid(row=8, column=4, sticky=W)

rkCklSubmit = Button(rekentool, text="Bevestigen", command=calcCirkel)
rkCklSubmit.grid(row=9, column=4, sticky=W)

#procent calculator
rkPctLabel = Label(rekentool, text="Bereken procent tussen 2 getallen")
rkPctLabel.grid(row=10, column=0, sticky=W, columnspan=2)

rkPctInput1Label = Label(rekentool, text="Getal 1")
rkPctInput1Label.grid(row=11, column=0, sticky=W)

rkPctInput2Label = Label(rekentool, text="Getal 2")
rkPctInput2Label.grid(row=11, column=1, sticky=W)

rkPctInput1 = Text(rekentool, width=10, height=1)
rkPctInput1.grid(row=12, column=0, sticky=W)

rkPctInput2 = Text(rekentool, width=10, height=1)
rkPctInput2.grid(row=12, column=1, sticky=W)

rkPctSubmit = Button(rekentool, text="Bevestigen", command=calcPct)
rkPctSubmit.grid(row=13, column=0, sticky=W)



#ontspanningstool
ontspanningstool = Frame(borderwidth=10)
label_1 = Label(ontspanningstool, text="ONSTPANNINGSTOOL", bg = "purple", fg="white", width=20, height=8)
label_1.pack()


#opdracht 3
opdr3 = Frame(borderwidth=10)

listbox_tasks=Listbox(opdr3, height=33, width=210)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks= Scrollbar(opdr3)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task=Entry(opdr3, width=212)
entry_task.pack()

#Buttons 
button_add_task = Button(opdr3, text='Taak Toevoegen', width=200, command=add_task)
button_add_task.pack()
button_delete_task = Button(opdr3, text='Taken Verwijderen', width=200, command=delete_task)
button_delete_task.pack()
button_load_task = Button(opdr3, text='Taken Laden', width=200, command=load_task)
button_load_task.pack()
button_save_task = Button(opdr3, text='Taken Opslaan', width=200, command=save_task)
button_save_task.pack()









window.mainloop()
