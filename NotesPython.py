#GorwinNotes
#импорт необходимых для работы программы модулей
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox
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
               cur.execute("INSERT INTO notes_table VALUES ('%s','%s','%s')" %(today, notes_title, notes))
               messagebox.showinfo(message="Заметка добавлена")
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
               sql_statement = "DELETE FROM notes_table" 
       else:
       #Удаляем заметки по названию и дате
               if (len(date) <=0) & (len(notes_title)<=0): 
                       #Raise error for no inputs
                       messagebox.showerror(message = "Просьба ввести корректные данные" )
                       return
               else:
                      sql_statement = "DELETE FROM notes_table where date ='%s' and notes_title ='%s'" %(date, notes_title)
       cur.execute(sql_statement)
       messagebox.showinfo(message="Заметки удалены")
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
               sql_statement = "UPDATE notes_table SET notes = '%s' where date ='%s' and notes_title ='%s'" %(notes, today, notes_title)
              
       cur.execute(sql_statement)
       messagebox.showinfo(message="Заявка обновлена")
       con.commit()              
       #Invoke call to class to view a window
window = Tk()
#Разрабатываем GUI
window.geometry("500x300")
window.title("Gorwin Notes")
#Заголовок окна программы & наименование, расположение и размер поля ввода даты 
title_label = Label(window, text="GORWIN NOTES. Приложение для работы с заметками").pack()
date_label = Label(window, text="Дата:").place(x=10,y=20)
date_entry = Entry(window,  width=20)
date_entry.place(x=50,y=20)
#Наименование, расположение и размер поля для вовода название заметки 
notes_title_label = Label(window, text="Название:").place(x=10,y=50)
notes_title_entry = Entry(window,  width=30)
notes_title_entry.place(x=80,y=50)
#Наименование, расположение и размер поля для вовода текста заметки
notes_label = Label(window, text="Текст:").place(x=10,y=90)
notes_entry = Text(window, width=50,height=5)
notes_entry.place(x=60,y=90)
 
#Кнопки и их функционал
button1 = Button(window,text='Добавить', bg = 'Turquoise',fg='Blue',command=add_notes).place(x=10,y=190)
button2 = Button(window,text='Просмотр', bg = 'Turquoise',fg='Blue',command=view_notes).place(x=110,y=190)
button3 = Button(window,text='Удалить', bg = 'Turquoise',fg='Blue',command=delete_notes).place(x=210,y=190)
button4 = Button(window,text='Обновить', bg = 'Turquoise',fg='Blue',command=update_notes).place(x=320,y=190)
 
#close the app
window.mainloop()
con.close()