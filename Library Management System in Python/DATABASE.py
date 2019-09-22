#code for the backend(database) of the project "LIBRARY - STORING OF BOOKS"

#import
import sqlite3

#define
def connect():
    """
    Connect function creates the database using SQLite3 library, and creates the table in the database with,
    ID, TITLE, AUTHOR, YEAR, ISBN columns
    """
    
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Book(id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert_data(title, author, year, isbn):
    '''
    Insert data inserts the user input into the table respectively
    '''
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO Book VALUES(NULL, ?,?,?,?)", (title,author,year,isbn))
    conn.commit()
    conn.close()
    view_data()

def view_data():
    '''
    View data displays all the contents in the listbox
    :return:
    '''
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_data(title="",author="",year="",isbn=""):
    '''
    Search data finds the row, containing the search parameter as entered by the user in the frontend GUI
    '''
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Book WHERE title = ? OR author = ? OR year = ? OR isbn = ?",(title,author,year,isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def del_data(id):
    '''
    Del data, deletes the data based on the selection of the user keyed in the frontend GUI
    '''
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Book WHERE id=?", (id,))
    conn.commit()
    conn.close()
    view_data()

def update_data(id,title,author,year,isbn):
    """
    Update data will update the respective column, either title, author, year or isbn as the case maybe, and user input.
    """
    conn = sqlite3.connect("BOOKSTORE.db")
    cur = conn.cursor()
    cur.execute("UPDATE Book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
    view_data()

#establish the connection with database
connect()


