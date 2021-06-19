from tkinter import *
import math

root = Tk()
root.title("Calculator")

title = Label(root, text="Welcome to your calculator!")
title.grid(row=0, column=0, columnspan=3)

numplay = Entry(root, width=25, borderwidth=3)
numplay.grid(row=1, column=0, columnspan=3, padx = 5, pady=5)

def buttonAssign(number):
    numCurr = numplay.get()
    numplay.delete(0, END)
    numplay.insert(0, str(numCurr) + str(number))
def buttonAdd():
    global flag
    global num1
    flag = 1
    num1 = float(numplay.get())
    numplay.delete(0, END)
def buttonSub():
    global flag
    global num1
    flag = 2
    num1 = float(numplay.get())
    numplay.delete(0, END)
def buttonMul():
    global flag
    global num1
    flag = 3
    num1 = float(numplay.get())
    numplay.delete(0, END)
def buttonDiv():
    global flag
    global num1
    flag = 4
    num1 = float(numplay.get())
    numplay.delete(0, END)
def buttonSqrt():
    num1 = float(numplay.get())
    numplay.delete(0, END)
    numplay.insert(0, math.sqrt(num1))
def buttonFac():
    num1 = int(numplay.get())
    numplay.delete(0, END)
    fact = 1
    i = 0
    for i in range(1, num1 + 1):
        fact = fact*i
    numplay.insert(0, fact)
def buttonEq():
    num2 = numplay.get()
    if flag == 1:
        numplay.delete(0, END)
        numplay.insert(0, num1 + float(num2))
    if flag == 2:
        numplay.delete(0, END)
        numplay.insert(0, num1 - float(num2))
    if flag == 3:
        numplay.delete(0, END)
        numplay.insert(0, num1 * float(num2))
    if flag == 4:
        try:
            numplay.insert(0, num1 / float(num2))
        except ZeroDivisionError:
            numplay.delete(0, END)
            numplay.insert(0, "Divison by 0 not possible!")
        else:
            numplay.delete(0, END)
            numplay.insert(0, num1 / float(num2))
def buttonClear():
    numplay.delete(0, END)

button1 = Button(root, text="1", padx=20, pady=10, command=lambda :buttonAssign(1))
button2 = Button(root, text="2", padx=20, pady=10, command=lambda :buttonAssign(2))
button3 = Button(root, text="3", padx=20, pady=10, command=lambda :buttonAssign(3))
button4 = Button(root, text="4", padx=20, pady=10, command=lambda :buttonAssign(4))
button5 = Button(root, text="5", padx=20, pady=10, command=lambda :buttonAssign(5))
button6 = Button(root, text="6", padx=20, pady=10, command=lambda :buttonAssign(6))
button7 = Button(root, text="7", padx=20, pady=10, command=lambda :buttonAssign(7))
button8 = Button(root, text="8", padx=20, pady=10, command=lambda :buttonAssign(8))
button9 = Button(root, text="9", padx=20, pady=10, command=lambda :buttonAssign(9))
button0 = Button(root, text="0", padx=20, pady=10, command=lambda :buttonAssign(0))
buttonEq = Button(root, text="=", padx=20, pady=10, command=buttonEq)
buttonAdd = Button(root, text="+", padx=20, pady=10, command=buttonAdd)
buttonSub =  Button(root, text=" -", padx=20, pady=10, command=buttonSub)
buttonMul = Button(root, text="*", padx=20, pady=10, command=buttonMul)
buttonDiv = Button(root, text="/", padx=20, pady=10, command=buttonDiv)
buttonSqrt = Button(root, text="sqrt", padx=13, pady=10, command=buttonSqrt)
buttonFac = Button(root, text="!", padx=21, pady=10, command=buttonFac)
buttonClear = Button(root, text="Clear", padx=65, pady=10, command=buttonClear)

button0.grid(row=6, column=1)

button1.grid(row=5, column=0)
button2.grid(row=5, column=1)
button3.grid(row=5, column=2)

button4.grid(row=4, column=0)
button5.grid(row=4, column=1)
button6.grid(row=4, column=2)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)

spacing = Label(root, text="")
spacing.grid(row=7, column=0, columnspan=3)
spacing.grid(row=8, column=0, columnspan=3)

buttonEq.grid(row=10, column=1)
buttonAdd.grid(row=9, column=1)
buttonSub.grid(row=11, column=1)
buttonMul.grid(row=10, column=0)
buttonDiv.grid(row=10, column=2)
buttonSqrt.grid(row=6, column=0)
buttonFac.grid(row=6, column=2)
buttonClear.grid(row=2, column=0, columnspan=3)

root.mainloop()
