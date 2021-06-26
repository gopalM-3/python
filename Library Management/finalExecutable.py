from tkinter import *
from datetime import date

# database
from LibData import *

# gui start
root = Tk()

root.title("Library Management")

title = Label(root, text="LIBRARY MANAGEMENT SERVICE")
title.grid(row=0, column=0)

# base window

# top window
def statusCheck():    
    check = Toplevel()
    check.title("Currently available")

    title = Label(check, text="Currently available books/journals")
    title.pack()

    c.execute('SELECT * FROM books')
    for i, j, k, l in c.fetchall():
        status = Label(check, text="There are " + str(j) + " copies of " + "'" + i + "' by " + "'" + k + "' available, it is '" + str(l) + "' pages long.")
        status.pack()

checkStatus = Label(root, text="Do you want to check the available books/journals?", anchor=E)
checkStatus.grid(row=1, column=0)
checkButton = Button(root, text="Show", padx=3, pady=3, command=statusCheck)
checkButton.grid(row=2, column=0)

frame = LabelFrame(root, padx=6, pady=6)
frame.grid(row=3, column=0, padx=6, pady=6)

nameLabel = Label(frame, text="Name: ", anchor=E)
nameLabel.grid(row=0, column=0)
nameEntry = Entry(frame, width=30, borderwidth=3)
nameEntry.grid(row=0, column=1)

authLabel = Label(frame, text="Author: ", anchor=E)
authLabel.grid(row=3, column=0)
authEntry = Entry(frame, width=30, borderwidth=3)
authEntry.grid(row=3, column=1)

pageLabel = Label(frame, text="No. of pages: ", anchor=E)
pageLabel.grid(row=4, column=0)
pageEntry = Entry(frame, width=30, borderwidth=3)
pageEntry.grid(row=4, column=1)

quantityLabel = Label(frame, text="Quantity (in numerals): ", anchor=E)
quantityLabel.grid(row=1, column=0)
quantityEntry = Entry(frame, width=30, borderwidth=3)
quantityEntry.grid(row=1, column=1)

Label(frame, text="What do you want to do?").grid(row=5, column=1)
status = IntVar()
add = Radiobutton(frame, text="Add this book(s) to the library", variable=status, value=1, anchor=E)
sub = Radiobutton(frame, text="Take this book(s) from the library", variable=status, value=0, anchor=E)
add.grid(row=6, column=1)
sub.grid(row=7, column=1)
status.set(None)

def confirmation():
    if status.get() == 1:
            c.execute('SELECT * FROM books')
            for i in c.fetchall():
                if i[0] == nameEntry.get():
                    addExistingBooks(nameEntry.get(), int(quantityEntry.get()))
                    Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully added!").grid(row=4, column=0)
                    break
                else:
                    addNewBooks(nameEntry.get(), int(quantityEntry.get()), authEntry.get(), pageEntry.get())
                    Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully added!").grid(row=4, column=0)
    else:
        c.execute('SELECT * FROM books')
        for i in c.fetchall():
            if i[0] == nameEntry.get():
                if i[1] > 0:
                    if i[1] - int(quantityEntry.get()) >= 0:
                        removeBooks(nameEntry.get(), int(quantityEntry.get()))
                        Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully removed!").grid(row=4, column=0)
                        break
                    else:
                        Label(root, text="Removing non-existing books not possible!").grid(row=4, column=0)
            else:
                Label(root, text="The book does not exist!").grid(row=4, column=0)

confirm = Button(frame, text="Confirm", padx=3, pady=3, command=confirmation)
confirm.grid(row=8, column=1)

Label(root, text="".center(69, '-')).grid(row=5, column=0)

frame2 = LabelFrame(root, text="Fine checker".center(14), padx=6, pady=6)
frame2.grid(row=6, column=0, padx=6, pady=6)

dateLabel = Label(frame2, text="Date of issue: (DD MM YYYY): ", anchor=E)
dateLabel.grid(row=0, column=0)
dateEntry = Entry(frame2, width=30, borderwidth=3)
dateEntry.grid(row=0, column=1)

def fineCheck():
    day = dateEntry.get().split()
    delta = date.today() - date(int(day[2]), int(day[1]), int(day[0]))
    Label(frame2, text="Your fine is " + str((delta.days)*1) + " rupees only.").grid(row=2, column=0)

confirm1 = Button(frame2, text="Confirm", padx=3, pady=3, command=fineCheck)
confirm1.grid(row=1, column=1)

root.mainloop()
c.connection.close()
