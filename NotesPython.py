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
# Вставляем строку данных
def add_notes():
       today = date_entry.get()
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       #Пропущенные значения
       if (len(today) <=0) & (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "Просьба ввести корректные данные" )
       else:
       #Insert into the table
               cur.execute("Вставить в notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
               messagebox.showinfo(message="Note added")
               con.commit() #Комитим
 #ОТОБРАЖЕНИЕ ЗАМЕТОК
def view_notes():
       date = date_entry.get()
       notes_title = notes_title_entry.get()
       if (len(date) <=0) & (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table"
       #Выборка по названию
       elif (len(date) <=0) & (len(notes_title)>0):
               sql_statement = "SELECT * FROM notes_table where notes_title ='%s'" %notes_title
       #Выборка по дате
       elif (len(date) >0) & (len(notes_title)<=0):
               sql_statement = "SELECT * FROM notes_table where date ='%s'"%date
       #Выборка по названию и дате
       else:
               sql_statement = "SELECT * FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
       cur.execute(sql_statement)
       row = cur.fetchall()
       if len(row)<=0:
               messagebox.showerror(message="Заметок не найдено")
       else:
               for i in row:
                       messagebox.showinfo(message="Date: "+i[0]+"\nTitle: "+i[1]+"\nNotes: "+i[2])
#УДАЛЕНИЕ ЗАМЕТОК
def delete_notes():
       date = date_entry.get()
       notes_title = notes_title_entry.get()
       #Удаляем все заметки
       choice = messagebox.askquestion(message="Вы хотите удалить все заметки?")
       if choice == 'yes':
               sql_statement = "Удалить из notes_table" 
       else:
       #Удаляем заметки по названию и дате
               if (len(date) <=0) & (len(notes_title)<=0): 
                       #Raise error for no inputs
                       messagebox.showerror(message = "Просьба ввести корректные данные" )
                       return
               else:
                      sql_statement = "Удалить из notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
       cur.execute(sql_statement)
       messagebox.showinfo(message="Note(s) Deleted")
       con.commit()
#ОБНОВЛЕНИЕ ЗАМЕТОК
def update_notes():
       today = date_entry.get()
       notes_title = notes_title_entry.get()
       notes = notes_entry.get("1.0", "end-1c")
       #Check if input is given by the user
       if (len(today) <=0) & (len(notes_title)<=0) & (len(notes)<=1):
               messagebox.showerror(message = "Просьба ввести корректные данные" )
       #update the note
       else:
               sql_statement = "Обновить notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)
              
       cur.execute(sql_statement)
       messagebox.showinfo(message="Заявка обновлена")
       con.commit()              
       