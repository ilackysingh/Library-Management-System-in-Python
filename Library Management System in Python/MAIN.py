#code for the frontend(G.U.I.)of the project "LIBRARY - STORING OF BOOKS"

#import
from tkinter import *
import DATABASE
import time

#define
def get_selected_row(event):
    """
    This function recieves the row, which the user has selected via list1.bind and passes it as "event" as arguements
    to get_selected_row, and return back the selected tuple for deletion.
    """
    try:
        #declared global var, since used by delete_command and list1.bind
        global selected_tuple
        # This gets the index of selected tuple from the listbox, curselection()[0], gets the data at index 0 of the tuple.
        index=list1.curselection()[0]       
        selected_tuple=list1.get(index)
        # empty the box for title
        e1.delete(0,END)
        # insert the entry of index[1] which is the title
        e1.insert(END,selected_tuple[1])
        # empty the box for author
        e2.delete(0,END)
        # insert the entry of index[1] which is the author
        e2.insert(END,selected_tuple[2])
        # empty the box for year
        e3.delete(0,END)
        # insert the entry of index[1] which is the year
        e3.insert(END,selected_tuple[3])
        # empty the box for isbn
        e4.delete(0,END)
        # insert the entry of index[1] which is the isbn
        e4.insert(END,selected_tuple[4])    
    except IndexError:
        # pass if there is an index error
        pass                                

def view_command():
    """
    This command triggers when the View All button is pressed, list1.delete erases the previous contents of the listbox
    The for loop traverses through the view_data() in the database script
    The list1.insert, inserts the data from the database into the list box as per ID.
    """
    list1.delete(0,END)
    for row in DATABASE.view_data():
        list1.insert(END,row)

def search_command():
    """
    Search command receives the parameter from user, i.e. the search parameter for title, author, year or isbn
    and every row realting to search data inserts into the listbox
    """
    list1.delete(0,END)
    for row in DATABASE.search_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)        

def insert_command():
    """
    Recieves the parameter to insert via get() for title or author or year or isbn.
    passes the value to database for insert into table
    """
    DATABASE.insert_data(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def update_command():
    """
    Recieves the update from the user through get() for either title, author, year, isbn as per user entry,
    passes the value to database for update of table
    """
    DATABASE.update_data(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())

def delete_command():
    """
    Recieves the selected_tuple after the user selects on the GUI and passes the value to database for deletion.
    """
    DATABASE.del_data(selected_tuple[0])

#G.U.I.

#Config    
window = Tk()
window.title("LIBRARY - STORING OF BOOKS")
window.geometry('600x300')
l0 = Label(window, text="LIBRARY - STORING OF BOOKS")        
l0.grid(row=0, column=0, columnspan=2)

def clock():
    t=time.strftime('%d-%m-%Y \n%H:%M:%S',time.localtime())
    if t!='':
        Label(window,text=t,font='times 10').grid(row=0,column=3)
    window.after(100,clock)
clock()

#button label for title
l1 = Label(window, text="Title")        
l1.grid(row=1, column=0)

#button label for author
l2 = Label(window, text="Author")      
l2.grid(row=1, column=2)

#button label for year
l3 = Label(window, text="Year")         
l3.grid(row=2, column=0)

#button label for ISBN
l4 = Label(window, text="ISBN")         
l4.grid(row=2, column=2)

#For user input of the title variable, and grid location of box
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=1, column=1)

#For user input of the author variable, and grid location of box
author_text = StringVar()
e2 = Entry(window, textvariable=author_text) 
e2.grid(row=1, column=3)

#For user input of the year variable, and grid location of box
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)  
e3.grid(row=2, column=1)

#For user input of the isbn variable, and grid location of box
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)  
e4.grid(row=2, column=3)

#Listbox declaration and grid location
list1 = Listbox(window, height=10, width=65)    
list1.grid(row=3, column=0, rowspan=6, columnspan=2)

#Scroll bar decleration
sb1 = Scrollbar(window)                 
sb1.grid(row=3, column=2, rowspan=6)

#Scroll bar assignment
list1.configure(yscrollcommand=sb1.set) 
sb1.configure(command=list1.yview)
list1.bind("<<ListboxSelect>>",get_selected_row)

#Button Declaration
b1 = Button(window, text='View All', width=12, command=view_command)
b1.grid(row=3, column=3)

b2 = Button(window, text='Search Entry', width=12, command=search_command)
b2.grid(row=4, column=3)

b3 = Button(window, text='Add Entry', width=12, command=insert_command)
b3.grid(row=5, column=3)

b4 = Button(window, text='Update Entry', width=12, command=update_command)
b4.grid(row=6, column=3)

b5 = Button(window, text='Delete Entry', width=12, command=delete_command)
b5.grid(row=7, column=3)

b6 = Button(window, text='Exit', width=12, command=window.destroy)
b6.grid(row=8, column=3)

#Tkinter method to keep the GUI active loop, until user closes the window
window.mainloop()    
