from tkinter import *

root = Tk()

root.title("Kalkulator")
root['bg'] = "black"
e = Entry(root, width=20,borderwidth=5,font=('Arial 22'))
e.grid(row=0,column=0,columnspan=3,padx = 10,pady=10)

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) +str(number))
def button_clear():
    e.delete(0,END)
def button_add():
    first_number =e.get()
    global f_num
    global math
    math = "addoction"
    f_num = int(first_number)
    e.delete(0,END)
def button_substract():

    first_number =e.get()
    global f_num
    global math
    math = "subtraction"

    f_num = int(first_number)
    e.delete(0,END)
def button_multiply():
    first_number =e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)
def button_divide():
    first_number =e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)
def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == "addoction":
        e.insert(0,f_num + int(second_number))
    if math == "subtraction":
        e.insert(0,f_num - int(second_number))
    if math == "multiplication":
        e.insert(0,f_num * int(second_number))
    if math == "division":
        wyn =f_num / int(second_number)
        e.insert(0,int(wyn))

#Definicja Przycisków
button_0 = Button(root,text="0",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda : button_click(0))
button_1 = Button(root,text="1",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(1))
button_2 = Button(root,text="2",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(2))
button_3 = Button(root,text="3",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(3))
button_4 = Button(root,text="4",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(4))
button_5 = Button(root,text="5",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(5))
button_6 = Button(root,text="6",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(6))
button_7 = Button(root,text="7",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(7))
button_8 = Button(root,text="8",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(8))
button_9 = Button(root,text="9",padx=47,pady=20,bg="white",font=('Arial 14'),command=lambda: button_click(9))
button_plus = Button(root,text="+",padx=46,pady=20,bg="white",font=('Arial 14'),command= button_add)
button_equal = Button(root,text="=",padx=110,pady=20,bg="white",font=('Arial 14'),command= button_equal)
button_clear = Button(root,text="Clear",padx=92,pady=20,bg="white",font=('Arial 14'),command= button_clear)

button_substract = Button(root,text="-",padx=49,pady=20,bg="white",font=('Arial 14'),command= button_substract)
button_multiply = Button(root,text="*",padx=50,pady=20,bg="white",font=('Arial 14'),command= button_multiply)
button_divide = Button(root,text="/",padx=50,pady=20,bg="white",font=('Arial 14'),command= button_divide)

#Wypisanuie przycisków
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_plus.grid(row=5,column=0)
button_equal.grid(row=5,column=1,columnspan=2)

button_substract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)
root.mainloop()