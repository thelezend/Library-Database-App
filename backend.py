# -*- coding: utf-8 -*-
"""
The backend script for Library Database App

@author: Lezend
"""

import sqlite3 #sqlite3 module is necessary for interacting with SQL databases

"""
Creates a new table if there is no existing one.
"""
def create_table():
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books (sno INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, book_id INTEGER)")
    conn.commit()
    conn.close()

"""
Inserts a new row into the table.
"""
def insert(title, author, year, book_id):
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, book_id))
    conn.commit()
    conn.close()
    
"""
Returns all the records from the table.
"""
def view():
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall() #stores fetched records in the "rows" varaible
    conn.close()
    return rows

"""
Searches for the record with a specific Title or Author or Year or Book_id
"""
def search(title = "", author = "", year = "", book_id = ""):
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR book_id = ?",
                (title, author, year, book_id))
    rows = cur.fetchall()
    conn.close()
    return rows

"""
Deletes the selected row from the List box.
"""
def delete(sno):
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE sno = ?", (sno,))
    conn.commit()
    conn.close()
    
"""
Updates the selected row from the List box with the new values.
"""
def update(sno, title, author, year, book_id):
    conn = sqlite3.connect("app database.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, book_id = ? WHERE sno = ?",
                (title, author, year, book_id, sno))
    conn.commit()
    conn.close()
    
    
create_table() #Creates table for the initial run if there is no existing table