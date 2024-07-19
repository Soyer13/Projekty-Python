from tkinter import *
from tkcalendar import Calendar, DateEntry
'''
from tkinter.ttk import *
'''
#pip install tkcalendar
if __name__ == '__main__':
    root = Tk()
    root.title('ToDo')
    root.iconbitmap('')
    root.geometry("540x600")
    root.minsize(540,400)
    root.configure(bg='White')

    #Wywoływanie zadania
    rowN = 2
    def dodaj(rowD):
        global TODO
        TODO = todo(rowD)
        global rowN
        rowN +=1
        print(rowN)

    #Tworzenie Menu
    TitleLabel = Label(root,text=" ToDo List",bg= '#404040',font=('System 20'),fg='#fff',padx=10,pady=20,border=0)
    #TitleLabelBc = Label(root,text=" ",bg="#1B1B1B",pady=20,padx=50)

    #button_save = Button(root, text="Zapisz", padx=10, pady=10, bg="#FFEA4A", fg='#fff', font=('System 20'))
    button_add = Button(root, text="Dodaj Zapis", padx=10, pady=10, bg="#19E359",fg='#fff', font=('System 20'),command=lambda:dodaj(rowN))
    #button_del = Button(root, text="Usuń Zapis", padx=10, pady=10, bg="#FE3538", fg='#fff', font=('System 20'))
    class todo:
        #Konstruktor
        def __init__(self,row):
            self.task(row)
        def task(self,row):
            '''photo = PhotoImage(file = r"Update.png")'''
            #Zmiene
            self.isTaskActiv = False
            self.isActiv = IntVar()

            #Definicja Obiektów
            #self.chceckbox = Checkbutton(root,variable=self.isActiv,bg='#fff')

            self.textbox = Text(root,width=30,height=2 , bg='#404040',fg='#19E359')

            self.DATE = DateEntry(root, width= 16, background= "#19E359", foreground= "black",bd=2,fg="#19E359")
            #TODO.DATE.get() wyciąganie wartości

            self.button_Done = Button(root, text="    ", padx=10, pady=10, bg="#19E359", fg='#404040', font=('System 14'),command=lambda: self.ISTASKACTIVE(self.isTaskActiv))
            #self.button_Update =  Button(root, text="Up", padx=10, pady=10, bg="#19E359", fg='#404040', font=('System 14'), command=lambda :print(TODO.DATE.get()))
            self.button_Del = Button(root, text="Del", padx=10, pady=10, bg="#FE3538", fg='#fff', font=('System 14'),command=lambda: self.delete())

            #Wyświetlenie Zadania
            #self.chceckbox.grid(row=row,column=1,padx=10,pady=10)
            self.button_Done.grid(row=row,column=1,padx=10,pady=10)
            self.textbox.grid(row=row,column=2,padx=10,pady=10,columnspan=3)
            self.DATE.grid(row=row,column=5,padx=10,pady=10,columnspan=2)
           # self.button_Update.grid(row=row,column=8,padx=10,pady=10)
            self.button_Del.grid(row=row,column=8,padx=10,pady=10)

        #Zmiana koloru przycisku Czerwone/Zielone
        def ISTASKACTIVE(self,ISTaskActive):
            if ISTaskActive == False:
                self.button_Done.configure(bg='#FE3538')
                self.isTaskActiv = True
            elif ISTaskActive== True:
                self.button_Done.configure(bg='#19E359')
                self.isTaskActiv = False

        #Usuwanie
        def delete(self):
            #self.chceckbox.destroy()
            self.button_Done.destroy()
            self.textbox.destroy()
            self.DATE.destroy()
           # self.button_Update.destroy()
            self.button_Del.destroy()




    TitleLabel.grid(row=1,column=1,columnspan=3,sticky='ew')
    #TitleLabelBc.grid(row=1, column=7,sticky='ew',columnspan=6)

    #button_save.grid(row=2,column=1,columnspan=3,sticky='ew')
    button_add.grid(row=1,column=4,columnspan=2,sticky='ew')
    #button_del.grid(row=2,column=6,columnspan=2)


    #TODO = todo()
    #TODO.task(3)




    root.mainloop()


