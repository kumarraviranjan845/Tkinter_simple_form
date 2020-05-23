from tkinter import *
import tkinter.messagebox
import os
import sqlite3

root = Tk()

root.geometry('2000x550')
root.title('MyApp')

my_menu = Menu(root)
root.config(menu = my_menu)

def open_menu():
    os.system('data.txt')

file_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'File', menu = file_menu)
file_menu.add_command(label = 'Open...', command = open_menu)
file_menu.add_separator()
file_menu.add_command(label = 'Exit', command = root.destroy)

def about_menu():
    tkinter.messagebox.showinfo('About MyApp', "MyApp is a simple GUI application using Tkinter in Python.")

help_menu = Menu(my_menu, tearoff = 0)
my_menu.add_cascade(label = 'Help', menu = help_menu)
help_menu.add_command(label = 'About MyAPP', command = about_menu)

topic_label = Label(root, text = 'Topic *', font=('Times New Roman', 16, 'bold')).place(x = 495, y = 50)
topic_entry = Text(root, height = 1, width = 50)
topic_entry.place(x = 495, y = 90)

description_label = Label(root, text = 'Description *', font = ('Times New Roman', 16, 'bold')).place(x = 495, y = 150)
description_entry = Text(root, height = 15, width = 50)
description_entry.place(x = 495, y = 190)
required_label = Label(root, text = '* Required', fg='red').place(x = 841, y = 435)

if topic_entry.get('1.0') != 0 or description_entry.get('1.0') != 0:
    Button(root, text = 'Save', relief = GROOVE, bg = 'yellow green', fg = 'black', font = ('Times New Roman', 12, 'bold'), padx = 8).place(x = 840 , y = 465)

def save_data():
    topic = topic_entry.get('1.0', 'end-1c')
    description = description_entry.get('1.0', 'end-1c')

    if len(topic) == 0 or len(description) == 0:
        tkinter.messagebox.showerror('Error', "Required fields can't be blank")
    else:
        with open('data.txt', 'a+') as file:
            file.write(topic + ' - ' + description + '\n')

        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('CREATE TABLE data(topic text, description text)')
        c.execute('INSERT INTO data VALUES(:topic, :description)', {'topic':topic_entry.get('1.0', 'end-1c'), 'description':description_entry.get('1.0', 'end-1c')})
        conn.commit()
        c.execute('SELECT * FROM data WHERE topic = :topic', {'topic': topic_entry.get("1.0", 'end-1c')})
        print(c.fetchall())
        conn.close()

        topic_entry.delete('1.0', END)
        description_entry.delete('1.0', END)

        tkinter.messagebox.showinfo('Data Saved', 'Data has been saved successfully...')

Button(root, text = 'Save', relief = GROOVE, bg = 'yellow green', fg = 'black', font = ('Times New Roman', 12, 'bold'),
                     command = save_data, padx = 8).place(x = 495 , y = 465)

def reset_data():
    topic_entry.delete('1.0', END)
    description_entry.delete('1.0', END)

Button(root, text = 'Reset', relief = GROOVE, bg = '#C0C0C0', fg = 'black', font = ('Times New Roman', 12, 'bold'),
                      command = reset_data, padx = 10).place(x = 560 , y = 465)

Button(root, text = 'Exit', relief = GROOVE, bg = 'red', fg = 'white', font = ('Times New Roman', 12, 'bold'),
                     command = root.destroy, padx = 8).place(x = 660, y = 465)

root.mainloop()
