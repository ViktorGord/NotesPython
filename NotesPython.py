#GorwinNotes
#импорт необходимых для работы программы модулей
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox
# Create database connection and connect to table
try:
       con = sql.connect('gorwin.db')
       cur = con.cursor()
       cur.execute('''CREATE TABLE notes_table
                        (date text, notes_title text, notes text)''')
except:
       print("Подключено к таблице базы данных")