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
import backend
window=Tk() #creates a window object
window.wm_title("BookStore") #for naming your window
l1=Label(window,text="Title")
l1.grid(row=0,column=0)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)



l2=Label(window,text="Author")
l2.grid(row=0,column=2)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)
def get_selected_row(event):
	try:
		global selected_tuple
		index=list1.curselection()[0]
		selected_tuple=list1.get(index)
		e1.delete(0,END)
		e1.insert(END,selected_tuple[1])
		e2.delete(0,END)
		e2.insert(END,selected_tuple[2])
		e3.delete(0,END)
		e3.insert(END,selected_tuple[3])
		e4.delete(0,END)
		e4.insert(END,selected_tuple[4])
	except IndexError:
		pass

def view_command():
	list1.delete(0,END)
	for row in backend.view():
		list1.insert(END,row)

def search_command():
	list1.delete(0,END)
	for row in backend.search(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()):
		list1.insert(END,row)
def insert_command():
	backend.insert(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
	list1.delete(0,END)
	list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),ISBN_text.get()))
def delete_command():
	backend.delete(selected_tuple[0])
	view_command()
	


def delete_all():
	backend.delete_all()
	list1.delete(0,END)

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),ISBN_text.get())
    view_command()
list1=Listbox(window,height=6,width=35)
list1.grid(row=2,column=1,rowspan=7)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=sb1.set)#set the  scroll command along the y-axis in the list
sb1.configure(command=list1.yview)
sb2 = Scrollbar(window, orient = HORIZONTAL)
sb2.grid(row=7, column = 1)
list1.configure(xscrollcommand=sb2.set)#set the  scroll command along the X-axis in the list
sb2.configure(command = list1.xview)

list1.bind('<<ListboxSelect>>',get_selected_row)
# widget.bind(event, handler)
#If an event matching the event description occurs in the widget, 
#the given handler is called with an object describing the event.
b1=Button(window,text="View all",width=12,command=view_command) #The command option takes a reference to a function
b1.grid(row=2,column=3)
b2=Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)
b3=Button(window,text="Add entry",width=12,command=insert_command)
b3.grid(row=4,column=3)
b4=Button(window,text="Update Selected",width=12,command=update_command)
b4.grid(row=5,column=3)
b5=Button(window,text="Delete Selected",width=12,command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window,text="Delete All",width=12,command=delete_all)
b6.grid(row=7,column=3)
b7=Button(window,text="Close",width=12,command=window.destroy)
b7.grid(row=8,column=3)

window.mainloop() #wrap up all the widgets


