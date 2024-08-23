from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

w = Tk()
w.title("IN BETWEEN")
w.geometry("1920x1080")
w.resizable(FALSE, FALSE)
w.attributes("-fullscreen", True)

frame = Frame(w)
frame.pack(side="top", expand=True, fill="both")

global i, e


def insert():
    order_id = o_id.get()
    item_name = i_name.get()
    platform = s_platform.get()
    quantity = qty.get()
    date_ordered = d_ordered.get()
    date_arrival = d_arrive.get()
    price = cost.get()

    if ((order_id == "Order ID" or order_id == "") or (item_name == "" or item_name == "Item Name") or (
            platform == "" or platform == "Shopping Platform") or
            (quantity == "" or quantity == "Quantity") or (date_ordered == "mm/dd/yy" or date_ordered == "") or (
                    date_arrival == "mm/dd/yy" or date_arrival == "") or
            (price == "Price" or price == "")):

        MessageBox.showinfo("ALERT", "Please enter all fields")
    else:
        con1 = mysql.connect(host="localhost", user="root", password="admin01",
                             database="records")
        cursor1 = con1.cursor()
        cursor1.execute(
            "INSERT INTO list VALUES('" + order_id + "', '" + item_name + "', '" + platform + "', '" + quantity + "',"
                                                                                                                  "'" + date_ordered + "', '" + date_arrival + "', '" + price + "')")
        cursor1.execute("commit")

        MessageBox.showinfo("Status", "Successfully Inserted")
        con1.close();


# total balance
con2 = mysql.connect(host="localhost", user="root", password="admin01",
                     database="records")
cursor2 = con2.cursor()
price = cursor2.execute("SELECT SUM(price) FROM list;")
results = cursor2.fetchall()
total_balance = ["PHP"] + results

con3 = mysql.connect(host="localhost", user="root", password="admin01",
                     database="records")
cursor3 = con3.cursor()
recents = Frame(frame, width=300, height=100, highlightbackground='white', highlightthickness=5)
recents.place(x=940, y=500)

def display():
    cursor3.execute("SELECT item_name, platform, date_arrival, price FROM records.list ORDER BY date_arrival ASC LIMIT 3")
    results_my_cursor = cursor3.fetchall()
    global i, e
    i=0
    for student in results_my_cursor:
        for j in range(len(student)):
            e = Label(recents, width=30, text=student[j],
                font=('arial', 12), anchor="w")
            e.grid(row=i, column=j, padx=6, pady=20)
            #e.place(x= 700, y=500)
        i=i+1


display()

def order_page():
    frame.destroy()

def history_page():
    pass
def close_page():
    w.quit()


o_id = Entry(frame, text="", font=('arial', 14), width=60, bd=1)
i_name = Entry(frame, text="", font=('arial', 14), width=60, bd=1)
s_platform = Entry(frame, text="", font=('arial', 14), width=25, bd=1)
qty = Entry(frame, text="", font=('arial', 14), width=25, bd=1)
d_ordered = Entry(frame, text="", font=('arial', 14), width=25, bd=1)
d_arrive = Entry(frame, text="", font=('arial', 14), width=25, bd=1)
cost = Entry(frame, text="", font=('arial', 14), width=60, bd=1)
price_label = Label(frame, text=total_balance, font=('Bebas Neue', 50), justify='center')
price_label.place(x=400, y=300)

add_order = Button(frame, text="Add Order", command=insert, font=('arial', 14), width=60)
orders = Button(frame, text="Orders", command=order_page, font=('arial', 14), width=20, height=10, bd=2)
history = Button(frame, text="History", command=history_page, font=('arial', 14), width=20, height=10, bd=2)
close = Button(frame, text="Close", command=close_page, font=('arial', 14), width=5, bd=2)

o_id.insert(0, "Order ID")
i_name.insert(0, "Item Name")
s_platform.insert(0, "Shopping Platform")
qty.insert(0, "Quantity")
d_ordered.insert(0, "mm/dd/yy")
d_arrive.insert(0, "mm/dd/yy")
cost.insert(0, "Price")

o_id.place(x=200, y=500)
i_name.place(x=200, y=550)
s_platform.place(x=200, y=600)
qty.place(x=588, y=600)
d_ordered.place(x=200, y=650)
d_arrive.place(x=588, y=650)
cost.place(x=200, y=700)
add_order.place(x=200, y=750)
orders.place(x=1150, y=150)
history.place(x=1450, y=150)
close.pack(side=TOP, anchor=NE)


w.mainloop()


def edit_data(id):  # display to edit and update record
    global i  # start row after the last line of display
    # collect record based on id and present for updation.
    row = cursor4.execute("SELECT * FROM records.listWHERE id=%s", id)
    s = row.fetchone()  # row details as tuple

    e1_str_id = StringVar(w)  # String variable
    e2_str_name = StringVar(w)
    e3_str_class = StringVar(w)
    e4_str_mark = StringVar(w)
    e5_str_gender = StringVar(w)

    e1_str_id.set(s[0])  # id is stored
    e2_str_name.set(s[1])  # Name is stored
    e3_str_class.set(s[2])  # class is stored
    e4_str_mark.set(s[3])  # mark is stored
    e5_str_gender.set(s[4])  # gender  is stored

    e1 = Entry(w, textvariable=e1_str_id, width=10, state='disabled')
    e1.grid(row=i, column=0)
    e2 = Entry(w, textvariable=e2_str_name, width=10)
    e2.grid(row=i, column=1)
    e3 = Entry(w, textvariable=e3_str_class, width=10)
    e3.grid(row=i, column=2)
    e4 = Entry(w, textvariable=e4_str_mark, width=10)
    e4.grid(row=i, column=3)
    e5 = Entry(w, textvariable=e5_str_gender, width=10)
    e5.grid(row=i, column=4)
    b2 = Button(w, text='Update', command=lambda: my_update(),
                relief='ridge', anchor="w", width=5)
    b2.grid(row=i, column=5)

    def my_update():  # update record
        data = (e2_str_name.get(), e3_str_class.get(), e4_str_mark.get(), e5_str_gender.get(), e1_str_id.get())
        id = cursor4.execute("UPDATE student SET name=%s,class=%s,\
            mark=%s,gender=%s WHERE id=%s", data)
        print("Row updated  = ", id.rowcount)
        for z in w.grid_slaves(i):  # remove the edit row
            w.grid_forget()
        display()  # refresh the data

        def edit_data(id):
            global i
            con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor4 = con4.cursor()
            cursor4.execute("SELECT * FROM records.list WHERE id=%s", id)
            s = cursor4.fetchone()  # row details as tuple

            e1_str_id = StringVar(w)  # String variable
            e2_str_name = StringVar(w)
            e3_str_class = StringVar(w)
            e4_str_mark = StringVar(w)
            e5_str_gender = StringVar(w)

            e1_str_id.set(s[0])  # id is stored
            e2_str_name.set(s[1])  # Name is stored
            e3_str_class.set(s[2])  # class is stored
            e4_str_mark.set(s[3])  # mark is stored
            e5_str_gender.set(s[4])  # gender  is stored

            e1 = Entry(order_list, textvariable=e1_str_id, width=10, state='disabled')
            e1.grid(row=i, column=0)
            e2 = Entry(order_list, textvariable=e2_str_name, width=10)
            e2.grid(row=i, column=1)
            e3 = Entry(order_list, textvariable=e3_str_class, width=10)
            e3.grid(row=i, column=2)
            e4 = Entry(order_list, textvariable=e4_str_mark, width=10)
            e4.grid(row=i, column=3)
            e5 = Entry(order_list, textvariable=e5_str_gender, width=10)
            e5.grid(row=i, column=4)
            b2 = Button(order_list, text='Update', command=lambda: my_update(),
                        relief='ridge', anchor="w", width=5)
            b2.grid(row=i, column=5)

            def edit_data(id):
                global i
                con5 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor5 = con5.cursor()
                cursor5.execute("SELECT * FROM records.list WHERE id = %s", id)
                s = cursor5.fetchone()  # row details as tuple

                e1_str_order_id = StringVar(w)  # String variable
                e2_str_item_name = StringVar(w)
                e3_str_platform = StringVar(w)
                e4_str_quantity = StringVar(w)
                e5_str_date_ordered = StringVar(w)
                e6_str_date_arrival = StringVar(w)
                e7_str_price = IntVar(w)

                e1_str_order_id.set(s[0])  # id is stored
                e2_str_item_name.set(s[1])  # Name is stored
                e3_str_platform.set(s[2])  # class is stored
                e4_str_quantity.set(s[3])  # mark is stored
                e5_str_date_ordered.set(s[4])
                e6_str_date_arrival.set(s[5])  # gender  is stored
                e7_str_price.set(s[6])

                e1 = Entry(order_frame_2, textvariable=e1_str_order_id, width=10, state='disabled')
                e1.grid(row=i, column=0)
                e2 = Entry(order_frame_2, textvariable=e2_str_item_name, width=10)
                e2.grid(row=i, column=1)
                e3 = Entry(order_frame_2, textvariable=e3_str_platform, width=10)
                e3.grid(row=i, column=2)
                e4 = Entry(order_frame_2, textvariable=e4_str_quantity, width=10)
                e4.grid(row=i, column=3)
                e5 = Entry(order_frame_2, textvariable=e5_str_date_ordered, width=10)
                e5.grid(row=i, column=4)
                e6 = Entry(order_frame_2, textvariable=e6_str_date_arrival, width=10)
                e6.grid(row=i, column=5)
                e7 = Entry(order_frame_2, textvariable=e7_str_price, width=10)
                e7.grid(row=i, column=6)

                b2 = Button(order_frame_2, text='Update', command=lambda: my_update(),
                            relief='ridge', anchor="w", width=5)
                b2.grid(row=i, column=5)


  def edit_data(order_id):
        global i
        con5 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
        cursor5 = con5.cursor()
        cursor5.execute("SELECT * FROM records.list WHERE order_id = %s", order_id)
        s = cursor5.fetchone()  # row details as tuple

        e1_str_order_id = StringVar(w)  # String variable
        e2_str_item_name = StringVar(w)
        e3_str_platform = StringVar(w)
        e4_str_quantity = StringVar(w)
        e5_str_date_ordered = StringVar(w)
        e6_str_date_arrival = StringVar(w)
        e7_str_price = IntVar(w)

        e1_str_order_id.set(s[0])  # id is stored
        e2_str_item_name.set(s[1])  # Name is stored
        e3_str_platform.set(s[2])  # class is stored
        e4_str_quantity.set(s[3])  # mark is stored
        e5_str_date_ordered.set(s[4])
        e6_str_date_arrival.set(s[5])  # gender  is stored
        e7_str_price.set(s[6])

        e1 = Entry(order_frame_2, textvariable=e1_str_order_id, width=10, state='disabled')
        e1.grid(row=i, column=0)
        e2 = Entry(order_frame_2, textvariable=e2_str_item_name, width=10)
        e2.grid(row=i, column=1)
        e3 = Entry(order_frame_2, textvariable=e3_str_platform, width=10)
        e3.grid(row=i, column=2)
        e4 = Entry(order_frame_2, textvariable=e4_str_quantity, width=10)
        e4.grid(row=i, column=3)
        e5 = Entry(order_frame_2, textvariable=e5_str_date_ordered, width=10)
        e5.grid(row=i, column=4)
        e6 = Entry(order_frame_2, textvariable=e6_str_date_arrival, width=10)
        e6.grid(row=i, column=5)
        e7 = Entry(order_frame_2, textvariable=e7_str_price, width=10)
        e7.grid(row=i, column=6)

        b2 = Button(order_frame_2, text='Update', command=lambda: my_update(),
                    relief='ridge', anchor="w", width=5)
        b2.grid(row=i, column=5)

