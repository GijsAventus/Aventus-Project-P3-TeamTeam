from tkinter import *
from tkinter import ttk, colorchooser

class main:
    def __init__(self,master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.drawWidgets()
        self.c.bind('<B1-Motion>',self.paint)
        self.c.bind('<ButtonRelease-1>',self.reset)

    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x,self.old_y,e.x,e.y,width=self.penwidth,fill=self.color_fg,capstyle=ROUND,smooth=True)

        self.old_x = e.x
        self.old_y = e.y

    def reset(self,e):   
        self.old_x = None
        self.old_y = None      

    def changeW(self,e): 
        self.penwidth = e 

    def clear(self):
        self.c.delete(ALL)

    def change_fg(self):  
        self.color_fg=colorchooser.askcolor(color=self.color_fg)[1]

    def change_bg(self):  
        self.color_bg=colorchooser.askcolor(color=self.color_bg)[1]
        self.c['bg'] = self.color_bg

    def drawWidgets(self):
        self.controls = Frame(self.master,padx = 5,pady = 5)
        Label(self.controls, text='Pen dikte:',font=('arial 18')).grid(row=0,column=0)
        self.slider = ttk.Scale(self.controls,from_= 5, to = 100,command=self.changeW,orient=VERTICAL)
        self.slider.set(self.penwidth)
        self.slider.grid(row=0,column=10,ipadx=1)
        self.controls.pack(side=LEFT)
        
        self.c = Canvas(self.master,width=500,height=400,bg=self.color_bg,)
        self.c.pack(fill=BOTH,expand=True)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        filemenu = Menu(menu)
        colormenu = Menu(menu)
        menu.add_cascade(label='Kleuren',menu=colormenu)
        colormenu.add_command(label='Verander kleur pen',command=self.change_fg)
        colormenu.add_command(label='Verander achterground kleur',command=self.change_bg)
        optionmenu = Menu(menu)
        menu.add_cascade(label='Opties',menu=optionmenu)
        optionmenu.add_command(label='Maak schoon',command=self.clear)
        optionmenu.add_command(label='Sluit',command=self.master.destroy) 
        
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.title('Application')
    root.mainloop()
