import sqlite3 
def connect():
	'''it is used to connect to the database books'''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id  integer PRIMARY KEY,title text,author text,year text,isbn integer)")
	conn.commit()
	conn.close()
def insert(title,author,year,isbn):
	''' it is used to inset into the database   '''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("INSERT INTO book values (Null,?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	conn.close()

def view():
	''' it is used to view all the enteries in the book table  of a books database  '''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book")
	rows=cur.fetchall()
	conn.close()
	return rows

def search(title="",author="",year="",isbn=""):
	''' it is used to search the entries
	 null string are passed so that user can select any one of them '''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
	conn.commit()
	rows=cur.fetchall()
	conn.close()
	return rows

def update(id,title,author,year,isbn):
	''' it updates the values according to the id selected in the user interface '''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
	conn.commit()
	conn.close()

def delete(id):
	''' deletes according to the id selected'''
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book WHERE id=?",(id,)) #(id,) commas has been used besides id so that it is passed as a tuple
	conn.commit()
	conn.close()
def delete_all():
	conn=sqlite3.connect("books.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM book")
	conn.commit()
	conn.close()

