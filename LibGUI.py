from tkinter import *

# database
books = {'LoTR 1': 3,
         'LoTR 2': 1,
         'LoTR 3': 2}

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

    for i, j in books.items():
        status = Label(check, text="There are " + str(j) + " copies of " + "'" + i + "'" + " available.")
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

quantityLabel = Label(frame, text="Quantity (in numerals): ", anchor=E)
quantityLabel.grid(row=1, column=0)
quantityEntry = Entry(frame, width=30, borderwidth=3)
quantityEntry.grid(row=1, column=1)

Label(frame, text="What do you want to do?").grid(row=2, column=1)
status = IntVar()
add = Radiobutton(frame, text="Add this book(s) to the library", variable=status, value=1, anchor=E)
sub = Radiobutton(frame, text="Take this book(s) from the library", variable=status, value=0, anchor=E)
add.grid(row=3, column=1)
sub.grid(row=4, column=1)
status.set(None)

def confirmation():
    if status.get() == 1:
            if nameEntry.get() in books:
                books[nameEntry.get()] += int(quantityEntry.get())
                Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully added!").grid(row=4, column=0)
            else:
                books.update({nameEntry.get(): int(quantityEntry.get())})
                Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully added!").grid(row=4, column=0)
    else:
        if nameEntry.get() in books:
            if books[nameEntry.get()] - int(quantityEntry.get()) >= 0:
                books[nameEntry.get()] -= int(quantityEntry.get())
                Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + " successully removed!").grid(row=4, column=0)
            else:
                Label(root, text="Removing non-existing books not possible!").grid(row=4, column=0)
        else:
            Label(root, text="The book does not exist!").grid(row=4, column=0)

confirm = Button(frame, text="Confirm", padx=3, pady=3, command=confirmation)
confirm.grid(row=5, column=1)

root.mainloop()