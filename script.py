# -*- coding: utf-8 -*-
"""
Library Database App
A program that stores book information:
    Title, Author
    Year, Book ID
    
User can:
    View all records
    Search an entry
    Add entry
    Update entry
    Delete

@author: Lezend
"""

#Tkinter is the most used GUI building module in Python
from tkinter import *
import backend

"""
Get the values of the selected row from listbox and fills them in the entry boxes.
"""
def get_selected_row(event): #Event parameter needs to be passed to bind the function with the Listboxselect event.
    if list1.curselection():
        global selected_tuple
        index = list1.curselection()[0] #Index of the selected item from the List box.
        selected_tuple = list1.get(index) #Values of the tuple in the list box with given index.
        clear_entries()
        #Fills the selected item values into the entry boxes.
        e1.insert(END, selected_tuple[1])
        e2.insert(END, selected_tuple[2])
        e3.insert(END, selected_tuple[3])
        e4.insert(END, selected_tuple[4])
    
"""
Clears the values present in the entry boxes.
"""
def clear_entries():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

"""
Lists all the rows of the table "books" in the listbox.
"""
def view_command():
    list1.delete(0, END) #Clears the list box.
    for row in backend.view():
        list1.insert(END, row) #Inserts new row at the end of the List box.
          
"""
Searches for a row which matches with any of the given entry.
"""
def search_command():
    list1.delete(0,END) #Clears the list box.
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), bookid_text.get()):
        list1.insert(END, row) #Inserts new row at the end of the List box.
    
"""
Adds a new row to the "books" table based on the values given typed in the entry boxes.
"""
def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), bookid_text.get())
    list1.delete(0, END) #Clears the list box.
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), bookid_text.get()))

"""
Updates the selected row with the values present in the entry boxes.
"""
def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), bookid_text.get())
    list1.delete(0, END) #Clears the list box.
    list1.insert(END, "Updated selected row!")
    for row in backend.view():
        list1.insert(END, row) #Inserts new row at the end of the List box.
    

"""
Deletes the selected row from the listbox.
"""
def delete_command():
    backend.delete(selected_tuple[0])
    clear_entries()
    list1.delete(0, END) #Clears the list box.
    list1.insert(END, "Deleted selected row!")
    for row in backend.view():
        list1.insert(END, row) #Inserts new row at the end of the List box.


window = Tk() #Creates the window object
window.wm_title("Library Database App")

#Label objects
l1 = Label(window, text = "Title")
l1.grid(row = 0, column = 0)
l2 = Label(window, text = "Author")
l2.grid(row = 0, column = 3)
l3 = Label(window, text = "Year")
l3.grid(row = 1, column = 0)
l4 = Label(window, text = "Book ID")
l4.grid(row = 1, column = 3)

#Entries are stored in these variables
title_text = StringVar()
author_text = StringVar()
year_text = StringVar()
bookid_text = StringVar()

#Entry boxes
e1 = Entry(window, textvariable = title_text)
e1.grid(row = 0, column = 1)
e2 = Entry(window, textvariable = author_text)
e2.grid(row = 0, column = 4)
e3 = Entry(window, textvariable = year_text)
e3.grid(row = 1, column = 1)
e4 = Entry(window, textvariable = bookid_text)
e4.grid(row = 1, column = 4)

#List box
list1 = Listbox(window, height = 15, width = 60)
list1.grid(row = 2, column = 0, rowspan = 7, columnspan = 5)

#Binding a function to the list box widget, <<ListboxSelect>> is the event type
list1.bind('<<ListboxSelect>>', get_selected_row)
    
#Scrollbar for the list box
sb1 = Scrollbar(window)
sb1.grid(row = 2, column = 5, rowspan = 7)

#Configuring scrollbar for the list box
list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

#Buttons
b1 = Button(window, text = "View all", width = 12, command = view_command)
b1.grid(row = 0, column = 6, rowspan = 2)
b2 = Button(window, text = "Search", width = 12, command = search_command)
b2.grid(row = 2, column = 6)
b3 = Button(window, text = "Add", width = 12, command = add_command)
b3.grid(row = 3, column = 6)
b4 = Button(window, text = "Update", width = 12, command = update_command)
b4.grid(row = 4, column = 6)
b5 = Button(window, text = "Delete", width = 12, command = delete_command)
b5.grid(row = 5, column = 6)
b6 = Button(window, text = "Exit", width = 12, command = window.destroy)
b6.grid(row = 6, column = 6)

view_command() #Lists all the rows on startup

window.mainloop() #Wraps up all the above widgets/objects

