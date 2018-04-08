"""
this program  stores book information
A book has the following attributes
title,author,year,ISBN

User can:

view all records
search an entry
add entry
update entry
delete
close
"""
from tkinter import *
from backend import Database # importing the database class.
#creating a blueprint of the database
database=Database("books.db")#creating an object of the database
class library(object):
    def __init__(self,window):
        self.window=window
        self.window.wm_title("BookStore") #for naming your window
        l1=Label(self.window,text="Title")
        l1.grid(row=0,column=0)
        self.title_text=StringVar()
        self.e1=Entry(self.window,textvariable=self.title_text)
        self.e1.grid(row=0,column=1)
        l2=Label(self.window,text="Author")
        l2.grid(row=0,column=2)

        self.author_text=StringVar()
        self.e2=Entry(self.window,textvariable=self.author_text)
        self.e2.grid(row=0,column=3)

        l3=Label(window,text="Year")
        l3.grid(row=1,column=0)

        self.year_text=StringVar()
        self.e3=Entry(window,textvariable=self.year_text)
        self.e3.grid(row=1,column=1)

        l4=Label(self.window,text="ISBN")
        l4.grid(row=1,column=2)
        self.ISBN_text=StringVar()
        self.e4=Entry(self.window,textvariable=self.ISBN_text)
        self.e4.grid(row=1,column=3)
        sb1=Scrollbar(self.window)
        sb1.grid(row=2,column=2,rowspan=6)
        self.list1=Listbox(self.window,height=6,width=35)
        self.list1.grid(row=2,column=1,rowspan=7)
        self.list1.configure(yscrollcommand=sb1.set)#set the  scroll command along the y-axis in the list
        sb1.configure(command=self.list1.yview)
        sb2 = Scrollbar(self.window, orient = HORIZONTAL)
        sb2.grid(row=7, column = 1)
        self.list1.configure(xscrollcommand=sb2.set)#set the  scroll command along the X-axis in the list
        sb2.configure(command = self.list1.xview)

        self.list1.bind('<<ListboxSelect>>',self.get_selected_row)
        # widget.bind(event, handler)
        #If an event matching the event description occurs in the widget, 
        #the given handler is called with an object describing the event.
        b1=Button(self.window,text="View all",width=12,command=self.view_command) #The command option takes a reference to a function
        b1.grid(row=2,column=3)
        b2=Button(self.window,text="Search entry",width=12,command=self.search_command)
        b2.grid(row=3,column=3)
        b3=Button(self.window,text="Add entry",width=12,command=self.insert_command)
        b3.grid(row=4,column=3)
        b4=Button(self.window,text="Update Selected",width=12,command=self.update_command)
        b4.grid(row=5,column=3)
        b5=Button(self.window,text="Delete Selected",width=12,command=self.delete_command)
        b5.grid(row=6,column=3)
        b6=Button(self.window,text="Delete All",width=12,command=self.delete_all)
        b6.grid(row=7,column=3)
        b7=Button(self.window,text="Close",width=12,command=self.window.destroy)
        b7.grid(row=8,column=3)

    def get_selected_row(self,event):
        try:
            global selected_tuple
            index=self.list1.curselection()[0]
            selected_tuple=self.list1.get(index)
            self.e1.delete(0,END)
            self.e1.insert(END,selected_tuple[1])
            self.e2.delete(0,END)
            self.e2.insert(END,selected_tuple[2])
            self.e3.delete(0,END)
            self.e3.insert(END,selected_tuple[3])
            self.e4.delete(0,END)
            self.e4.insert(END,selected_tuple[4])
        except IndexError:
            pass

    def view_command(self):
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)

    def search_command(self):
        self.list1.delete(0,END)
        for row in database.search(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.ISBN_text.get()):
            self.list1.insert(END,row)
    def insert_command(self):
        database.insert(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.ISBN_text.get())
        self.list1.delete(0,END)
        self.list1.insert(END,(self.title_text.get(),self.author_text.get(),self.year_text.get(),self.ISBN_text.get()))
    def delete_command(self):
        database.delete(selected_tuple[0])
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
    def delete_all(self):
        database.delete_all()
        self.list1.delete(0,END)
    def update_command(self):
        database.update(selected_tuple[0],self.title_text.get(),self.author_text.get(),self.year_text.get(),self.ISBN_text.get())
        self.list1.delete(0,END)
        for row in database.view():
            self.list1.insert(END,row)
        

window=Tk() #creates a window object
Library=library(window)
window.mainloop() #wrap up all the widgets

