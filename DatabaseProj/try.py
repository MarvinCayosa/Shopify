import tkinter as tk
from tkinter import *
import mysql.connector as mysql

my_w = tk.Tk()
my_w.geometry("450x350")
global i

con = mysql.connect(host="localhost", user="root", password="admin01",
                    database="records")
cursor = con.cursor()

def display():

    cursor.execute("SELECT * FROM records.list")
    results_my_cursor = cursor.fetchall()
    global i
    i = 0
    for x in results_my_cursor:
        for j in range(len(x)):
            e = Label(my_w, width=10, text=x[j],
                      relief='ridge', anchor="w")
            e.grid(row=i, column=j)
            # e.insert(END, student[j])
        e = tk.Button(my_w, width=5, text='Edit', relief='ridge',
                      anchor="w", command=lambda k=x[0]: edit_data(k))
        e.grid(row=i, column=5)
        i = i + 1

display()

def edit_data(order_id):  # display to edit and update record
    global i  # start row after the last line of display
    # collect record based on id and present for updation.
    mydb = mysql.connect(host="localhost", user="root", password="admin01", database="records")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM records.list WHERE order_id=" + order_id)
    s = mycursor.fetchone()  # row details as tuple

    e1_str_id = tk.StringVar(my_w)  # String variable
    e2_str_name = tk.StringVar(my_w)
    e3_str_class = tk.StringVar(my_w)
    e4_str_mark = tk.StringVar(my_w)
    e5_str_gender = tk.StringVar(my_w)

    e1_str_id.set(s[0])  # id is stored
    e2_str_name.set(s[1])  # Name is stored
    e3_str_class.set(s[2])  # class is stored
    e4_str_mark.set(s[3])  # mark is stored
    e5_str_gender.set(s[4])  # gender  is stored

    e1 = tk.Entry(my_w, textvariable=e1_str_id, width=10, state='disabled')
    e1.grid(row=i, column=0)
    e2 = tk.Entry(my_w, textvariable=e2_str_name, width=10)
    e2.grid(row=i, column=1)
    e3 = tk.Entry(my_w, textvariable=e3_str_class, width=10)
    e3.grid(row=i, column=2)
    e4 = tk.Entry(my_w, textvariable=e4_str_mark, width=10)
    e4.grid(row=i, column=3)
    e5 = tk.Entry(my_w, textvariable=e5_str_gender, width=10)
    e5.grid(row=i, column=4)
    b2 = tk.Button(my_w, text='Update', command=lambda: my_update(),
                   relief='ridge', anchor="w", width=5)
    b2.grid(row=i, column=5)

    def my_update():  # update record
        data = (e2_str_name.get(), e3_str_class.get(), e4_str_mark.get(), e5_str_gender.get(), e1_str_id.get())
        id = cursor.execute("UPDATE records.list SET name=%s,class=%s,\
            mark=%s,gender=%s WHERE id=%s", data)
        print("Row updated  = ", id.rowcount)
        for w in my_w.grid_slaves(i):  # remove the edit row
            w.grid_forget()
        display()  # refresh the data


my_w.mainloop()