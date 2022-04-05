from tkinter import *
import tkinter.messagebox
import pickle 

root =Tk()
root.title('To-do lijst')
root.geometry('600x400')

def add_task():
    task= entry_task.get()
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


#Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks=tkinter.Listbox(frame_tasks, height=33, width=210)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks= tkinter.Scrollbar(frame_tasks )
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)
#50 kleine width
entry_task=tkinter.Entry(root, width=212)
entry_task.pack()
#48 kleine width
button_add_task = tkinter.Button(root, text='Taak Toevoegen', width=200, command=add_task)
button_add_task.pack()
button_delete_task = tkinter.Button(root, text='Taken Verwijderen', width=200, command=delete_task)
button_delete_task.pack()
button_load_task = tkinter.Button(root, text='Taken Laden', width=200, command=load_task)
button_load_task.pack()
button_save_task = tkinter.Button(root, text='Taken Opslaan', width=200, command=save_task)
button_save_task.pack()

root.mainloop()
