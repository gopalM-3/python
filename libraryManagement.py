from tkinter import *

# database
books = {'Programming in C: Pradip Dey Manas Ghosh': 1,
         'Programming Python, 4th Edition : Mark Lutz':1,
         'Animal Farm: George Orwell': 1,
         'Alice in Wonderland: Lewis Carrol': 1,
         'Discovery of India: Pandit Jawaharlal Nehru': 1,
         'Geetanjali: Rabindra Nath Tagore':1,
         'Raghuvamsa: Kalidas':1,
         'Avigyan Sakuntalam : Kalidas':1,
         'Shakuntala: Kalidas':1,
         'The Merchant of Venice: Shakespeare':1,
         'Antony and Cleopatra: Shakespeare':1,
         'A Tale of Two Cities – Charles Dickens':1,
         'David Copperfield – Charles Dickens':1,
         'Geetanjali: Rabindra Nath Tagore':1,
         'One Day in the Life of Ivan Denisovich: Alexander Solzhenitsyn':1,
         'Utopia: Sir Thomas Moor':1,	
         'Crime and Punishment: Dostoevsky':1,
         'Origin of Species: Charles Darwin':1}
types={'Programming in C: Pradip Dey Manas Ghosh':'Paperback',
       'Programming Python, 4th Edition : Mark Lutz':'Paperback',
        'Animal Farm: George Orwell':'Paperback',
         'Alice in Wonderland: Lewis Carrol': 'Loose Leaf',
         'Discovery of India: Pandit Jawaharlal Nehru': 'Paperback',
         'Geetanjali: Rabindra Nath Tagore': 'Hardcover',
         'Raghuvamsa: Kalidas':'Paperback',
         'Avigyan Sakuntalam : Kalidas':'Paperback',
         'Shakuntala: Kalidas': 'Paperback',
         'The Merchant of Venice: Shakespeare':'Loose Leaf',
         'Antony and Cleopatra: Shakespeare':'Loose Leaf',
         'A Tale of Two Cities – Charles Dickens':'Hardcover',
         'David Copperfield – Charles Dickens':'Hardcover',
         'Geetanjali: Rabindra Nath Tagore':'Hardcover',
         'One Day in the Life of Ivan Denisovich: Alexander Solzhenitsyn':'Paperback',
         'Utopia: Sir Thomas Moor':'Loose Leaf',	
         'Crime and Punishment: Dostoevsky':'Paperback',
         'Origin of Species: Charles Darwin': ' Hardcover'}

pages = {'Programming in C: Pradip Dey Manas Ghosh': 350,
         'Programming Python, 4th Edition : Mark Lutz':500,
         'Animal Farm: George Orwell': 175,
         'Alice in Wonderland: Lewis Carrol': 200,
         'Discovery of India: Pandit Jawaharlal Nehru': 500,
         'Geetanjali: Rabindra Nath Tagore':525,
         'Raghuvamsa: Kalidas':200,
         'Avigyan Sakuntalam : Kalidas':175,
         'Shakuntala: Kalidas':125,
         'The Merchant of Venice: Shakespeare':75,
         'Antony and Cleopatra: Shakespeare':100,
         'A Tale of Two Cities – Charles Dickens':90,
         'David Copperfield – Charles Dickens':125,
         'Geetanjali: Rabindra Nath Tagore':335,
         'One Day in the Life of Ivan Denisovich: Alexander Solzhenitsyn':50,
         'Utopia: Sir Thomas Moor':150,	
         'Crime and Punishment: Dostoevsky':100,
         'Origin of Species: Charles Darwin':650}
         
                                               


         

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

    for j in types.items():
        for k in pages.items():
           status=Label(check, text= str(k)+ "pages"+ " Book is of " + "'" + str(j) + "'" + "type"   )
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

authorLabel = Label(frame, text="Author : ", anchor=E)
authorLabel.grid(row=2, column=0)
authorEntry = Entry(frame, width=30, borderwidth=3)
authorEntry.grid(row=2, column=1)

pagesLabel = Label(frame, text="No.of Pages: ", anchor=E)
pagesLabel.grid(row=3, column=0)
pagesEntry = Entry(frame, width=30, borderwidth=3)
pagesEntry.grid(row=3, column=1)

bookLabel = Label(frame, text=" Type of Book: ", anchor=E)
bookLabel.grid(row=4, column=0)
bookEntry = Entry(frame, width=30, borderwidth=3)
bookEntry.grid(row=4, column=1)

            


Label(frame, text="What do you want to do?").grid(row=6, column=1)
status = IntVar()
add = Radiobutton(frame, text="Return this book(s) to the library", variable=status, value=1, anchor=E)
sub = Radiobutton(frame, text="Take this book(s) from the library", variable=status, value=0, anchor=E)
add.grid(row=7, column=1)
sub.grid(row=8, column=1)
status.set(None)

def confirmation():
    if status.get() == 1:
            if nameEntry.get() in books:
                 if typesEntry.get() in types:
                    books[nameEntry.get()] += int(quantityEntry.get())
                    Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + typesEntry.get()+ " successully returned!").grid(row=5, column=0)
            else:
                books.update({nameEntry.get(): int(quantityEntry.get())})
                Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + typesEntry.get()+" successully returned!").grid(row=5, column=0)
    else:
        if nameEntry.get() in books:
            if typesEntry.get() in types:
                if books[nameEntry.get()] - int(quantityEntry.get()) >= 0:
                   books[nameEntry.get()] -= int(quantityEntry.get())
                   Label(root, text=quantityEntry.get() + " copies of " + nameEntry.get() + typesEntry.get()+" taken successully !").grid(row=5, column=0)
            else:
                Label(root, text="Removing non-existing books not possible!").grid(row=5, column=0)
        else:
            Label(root, text="The book does not exist!").grid(row=5, column=0)

confirm = Button(frame, text="Confirm", padx=3, pady=3, command=confirmation)
confirm.grid(row=5, column=1)

root.mainloop()

