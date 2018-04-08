import sqlite3 
class Database:
	#A class can be thought of as a 'blueprint' for objects
	def __init__(self,db):
		'''initializing an object(Constructor).
			These line of code will always be executed whenever the above class is called
			it is used to connect to the database books.
			self variable refers to the object itself.
		'''
		self.conn=sqlite3.connect(db)
		self.cur=self.conn.cursor()
		self.cur.execute("CREATE TABLE IF NOT EXISTS book(id  integer PRIMARY KEY,title text,author text,year text,isbn integer)")
		self.conn.commit()
	def insert(self,title,author,year,isbn):
		''' it is used to inset into the database   '''
		#the class sends the object instance to this method.Hence self should be included
		self.cur.execute("INSERT INTO book values (Null,?,?,?,?)",(title,author,year,isbn))
		self.conn.commit()
		
	def view(self):
		''' it is used to view all the enteries in the book table  of a books database  '''
		#the class sends the object instance to this method.Hence self should be included
		self.cur.execute("SELECT * FROM book")
		rows=self.cur.fetchall()
		
		return rows

	def search(self,title="",author="",year="",isbn=""):
		''' it is used to search the entries
		 null string are passed so that user can select any one of them '''
		self.cur.execute("SELECT * FROM book where title=? or author=? or year=? or isbn=?",(title,author,year,isbn))
		self.conn.commit()
		rows=self.cur.fetchall()
		
		return rows

	def update(self,id,title,author,year,isbn):
		''' it updates the values according to the id selected in the user interface '''
		self.cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
		self.conn.commit()
		
		

	def delete(self,id):
		''' deletes according to the id selected'''
		self.cur.execute("DELETE FROM book WHERE id=?",(id,)) #(id,) commas has been used besides id so that it is passed as a tuple
		self.conn.commit()
	def delete_all(self):
		self.cur.execute("DELETE FROM book")
		self.conn.commit()
		
	def __del__(self): #destructing your object
		''' This method is applied when this instance(database=Database("books.db")) is deleted
		from the script i.e. when you exit the script '''
		self.conn.close()

