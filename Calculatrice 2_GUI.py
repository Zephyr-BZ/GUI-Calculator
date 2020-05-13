from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(width= 40, borderwidth= 20, bg= 'black', fg= 'white')
e.grid(row= 0, column= 0, columnspan= 4, padx= 10, pady=5)

def add_num(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def clear():
    e.delete(0,END)

def divide():
    num_1 = e.get()
    sym = '/'
    e.delete(0, END)
    e.insert(0, num_1 + sym)

def plus():
    num_1 = e.get()
    sym = '+'
    e.delete(0, END)
    e.insert(0, num_1 + sym)

def minus():
    num_1 = e.get()
    sym = '-'
    e.delete(0, END)
    e.insert(0, num_1 + sym)

def multiply():
    num_1 = e.get()
    sym = '*'
    e.delete(0, END)
    e.insert(0, num_1 + sym)

def equal():
    final_num = e.get()
    answer = str(eval(final_num))
    e.delete(0, END)
    
    e.insert(0, answer)

# Create the buttons

but_1 = Button(root, text= '1', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(1))
but_2 = Button(root, text= '2', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(2))
but_3 = Button(root, text= '3', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(3))
but_4 = Button(root, text= '4', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(4))
but_5 = Button(root, text= '5', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(5))
but_6 = Button(root, text= '6', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(6))
but_7 = Button(root, text= '7', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(7))
but_8 = Button(root, text= '8', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(8))
but_9 = Button(root, text= '9', padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(9))
but_0 = Button(root, text= '0', padx= 67, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(0))

but_divide = Button(root, text= "/", padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= divide)
but_plus = Button(root, text= "+", padx= 29, pady= 62, bg= "paleturquoise", bd= 2, command= plus)
but_x = Button(root, text= "*", padx= 30, pady= 25, bg= "paleturquoise", bd= 2, command= multiply)
but_minus = Button(root, text= "-", padx= 29, pady= 25, bg= "paleturquoise", bd= 2, command= minus)

p_open = Button(root, text= '(', padx= 69, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num("("))
p_close = Button(root, text= ')', padx= 69, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num(")"))

but_C = Button(root, text= "C", padx= 29, pady= 25, bg= "paleturquoise", bd= 2, command= clear)
but_equal = Button(root, text= "=", padx= 29, pady= 62, bg= "paleturquoise", bd= 2, command= equal)
but_dot = Button(root, text= ".", padx= 32, pady= 25, bg= "paleturquoise", bd= 2, command= lambda: add_num('.'))

# Place the buttons

but_C.grid(row=1, column=0)
but_divide.grid(row= 1, column= 1)
but_plus.grid(row= 2, column= 3, rowspan= 2)
but_x.grid(row= 1, column= 2)
but_minus.grid(row= 1, column= 3)

but_7.grid(row= 2, column= 0)
but_8.grid(row= 2, column= 1)
but_9.grid(row= 2, column= 2)

but_4.grid(row= 3, column= 0)
but_5.grid(row= 3, column= 1)
but_6.grid(row= 3, column= 2)

but_1.grid(row= 4, column= 0)
but_2.grid(row= 4, column= 1)
but_3.grid(row= 4, column= 2)

but_0.grid(row= 5, column= 0, columnspan= 2)
but_dot.grid(row= 5, column= 2)
but_equal.grid(row= 4, column= 3, rowspan= 2)

p_open.grid(row= 6, column= 0, columnspan= 2)
p_close.grid(row= 6, column= 2, columnspan= 2)


root.mainloop()