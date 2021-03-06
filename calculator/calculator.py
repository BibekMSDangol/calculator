from tkinter import *

root = Tk()

root.title("Calculator")
root.configure(background='skyblue')

e = Entry(root, width=40)
e.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_add():
    first_number=e.get()
    global f_num
    global math
    math = "addition"
    f_num=int(first_number)
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)


one = PhotoImage(file='one.png')
two = PhotoImage(file='two.png')
three = PhotoImage(file='three.png')
four = PhotoImage(file='four.png')
five = PhotoImage(file='five.png')
six = PhotoImage(file='six.png')
seven = PhotoImage(file='seven.png')
eight = PhotoImage(file='eight.png')
nine = PhotoImage(file='nine.png')
zero = PhotoImage(file='zero.png')
add = PhotoImage(file='plus.png')
sub = PhotoImage(file='minus.png')
mul = PhotoImage(file='Multi.png')
div = PhotoImage(file='divide.png')
clear = PhotoImage(file='clear.png')
equals = PhotoImage(file='equals.png')


button_1 = Button(root,image=one, border=0, command=lambda : button_click(1))
button_2 = Button(root, image=two, border=0, command=lambda : button_click(2))
button_3 = Button(root, image=three, border=0, command=lambda : button_click(3))
button_4 = Button(root, image=four, border=0, command=lambda : button_click(4))
button_5 = Button(root, image=five, border=0, command=lambda : button_click(5))
button_6 = Button(root, image=six, border=0, command=lambda : button_click(6))
button_7 = Button(root, image=seven, border=0, command=lambda : button_click(7))
button_8 = Button(root, image=eight, border=0, command=lambda : button_click(8))
button_9 = Button(root, image=nine, border=0, command=lambda : button_click(9))
button_0 = Button(root, image=zero, border=0, command=lambda : button_click(0))
button_add = Button(root, image=add, command=button_add, border=0)
button_subtract = Button(root, image=sub, command=button_subtract, border=0)
button_multiply = Button(root, image=mul, command=button_multiply, border=0)
button_divide = Button(root, image=div, command=button_divide, border=0)
button_equal = Button(root, image=equals, command=button_equal, border=0)
button_clear = Button(root, image=clear, command=button_clear, border=0, height=96, width=100)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)
button_clear.grid(row= 4, column=0)
button_divide.grid(row=1, column=3)
button_multiply.grid(row=2, column=3)
button_subtract.grid(row=3, column=3)
button_add.grid(row=4, column=3)
button_equal.grid(row=4, column=2)



root.mainloop()


