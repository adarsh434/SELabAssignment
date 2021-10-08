from tkinter import *
import sqlite3

root = Tk()
root.geometry('600x500')
root.title("Registration Page")

Username = StringVar()
Password = StringVar()

def database():
    name = Username.get()
    password = Password.get()
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Students (Fullname TEXT, Password TEXT)')
    cursor.execute('INSERT INTO Students (Fullname, Password) VALUES(?,?)', (name, password))
    conn.commit()

label_0 = Label(root, text="Registration Page", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_1 = Label(root, text="Username", width=20, font=("bold", 10))
label_1.place(x=80, y=130)

entry_1 = Entry(root, textvar = Username)
entry_1.place(x=240, y=130)

label_1 = Label(root, text="Password", width=20, font=("bold", 10))
label_1.place(x=68, y=180)

entry_1 = Entry(root, textvar = Password)
entry_1.place(x=240, y=180)

Button(root, text="Submit", width=20, bg='#00FF00', fg='white', command=database).place(x=180, y=380)

root.mainloop()

