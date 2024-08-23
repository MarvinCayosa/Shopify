from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

w = Tk()
w.title("Spendify")
w.geometry("1366x768")
w.resizable(FALSE, FALSE)
# w.attributes('-fullscreen',True)

bg = PhotoImage(file='home_bg.png')
button_add = PhotoImage(file='add.png')
orders_button = PhotoImage(file='o_button.png')
history_button = PhotoImage(file='H_button.png')
close_button = PhotoImage(file='x_button.png')
order_bg = PhotoImage(file='order_bg.png')
back_button = PhotoImage(file='back_btn.png')
back_button2 = PhotoImage(file='back_btn2.png')
search_btn = PhotoImage(file='search_button.png')
edit_button = PhotoImage(file='edit_btn.png')
delete_button = PhotoImage(file='delete_btn.png')
update_button = PhotoImage(file='update_button.png')
cancel_button = PhotoImage(file='cancel_button.png')
history_bg = PhotoImage(file='order_history.png')
landing_bg = PhotoImage(file='landing bg2.png')
start_bt = PhotoImage(file='start.png')
login = PhotoImage(file='login.png')
sign_up = PhotoImage(file='Sign-up.png')
login_bg = PhotoImage(file='login_bg.png')
sign_up_bg = PhotoImage(file='signup_bg.png')
login_btn = PhotoImage(file='login_cont.png')
sign_up_btn = PhotoImage(file='create_acc.png')
clear_history_btn = PhotoImage(file='clear_history.png')

global i, order_frame, history_frame, price, total_bal, price_label, str_date_arrival, user, back
global entry1, entry2, entry3, entry4, entry5, entry6, entry7, update_frame, sign_up_frame, login_frame, flt_price
global str_order_id, str_item_name, str_platform, str_quantity, str_date_ordered, email_ac, j, price_label2

landing_frame = Frame(w, bg='#ffffff')
landing_frame.pack(side="top", expand=True, fill="both")
canvas_land = Canvas(landing_frame)
canvas_land.pack(side="left", expand=True, fill="both")
canvas_land.create_image(685, 386, image=landing_bg)


def create_account():
    global sign_up_frame, login_frame, user
    landing_frame.pack_forget()

    sign_up_frame = Frame(w, bg='#ffffff')
    sign_up_frame.pack(side="top", expand=True, fill="both")

    canvas_sign = Canvas(sign_up_frame)
    canvas_sign.pack(side="left", expand=True, fill="both")
    canvas_sign.create_image(685, 386, image=sign_up_bg)

    def insert_info():
        global user, email_ac
        user = username.get()
        email_ac = email.get()
        passw = password.get()

        try:
            if (user == "Username" or user == "") or (email_ac == "" or email_ac == "Email") \
                    or (passw == "" or passw == "Password"):
                MessageBox.showinfo("ALERT", "Please enter all fields")

            else:
                con1 = mysql.connect(host="localhost", user="root", password="admin01",
                                     database="records")
                cursor1 = con1.cursor()
                cursor1.execute("INSERT INTO records.account "
                                "VALUES('" + user + "', '" + email_ac + "', '" + passw + "')")
                cursor1.execute("commit")
                MessageBox.showinfo("Status", "Successfully Created a New Account")
                con1.close()
                if MessageBox.showinfo:
                    sign_up_frame.pack_forget()
                    landing_frame.pack(side="top", expand=True, fill="both")

        except:
            MessageBox.showinfo("Status", "Cannot Have Duplicate Accounts")

    show_ck = IntVar(value=0)

    def show_pass():
        if show_ck.get() == 1:
            password.config(show='')
        else:
            password.config(show='*')

    username = Entry(sign_up_frame, font=('Roboto', 9), width=40, bd=0)
    email = Entry(sign_up_frame, font=('Roboto', 9), width=40, bd=0)
    password = Entry(sign_up_frame, show='*', font=('Roboto', 9), width=40, bd=0)
    create_ac = Button(sign_up_frame, image=sign_up_btn, command=insert_info, bd=0, bg='white')
    back_btn = Button(sign_up_frame, image=back_button2, command=back_1, bd=0, bg='white')
    show_password = Checkbutton(sign_up_frame, text="Show Password",
                                variable=show_ck, command=show_pass,
                                font=('arial', 9), offvalue=0, onvalue=1, bg='white')

    username.place(x=218, y=345)
    email.place(x=218, y=418)
    password.place(x=218, y=492)
    create_ac.place(x=205, y=560)
    back_btn.place(x=15, y=10)
    show_password.place(x=207, y=526)


def login_page():
    global login_frame
    landing_frame.pack_forget()

    login_frame = Frame(w, bg='#ffffff')
    login_frame.pack(side="top", expand=True, fill="both")
    canvas_log = Canvas(login_frame)
    canvas_log.pack(side="left", expand=True, fill="both")
    canvas_log.create_image(685, 386, image=login_bg)

    def login_acc():
        global email_ac, user
        user = username.get()
        email_ac = email.get()
        passw = password.get()

        if (user == "Username" or user == "") or (email_ac == "" or email_ac == "Email") or (
                passw == "" or passw == "Password"):
            MessageBox.showinfo("ALERT", "Please enter all fields")

        else:
            con1 = mysql.connect(host="localhost", user="root", password="admin01",
                                 database="records")
            cursor1 = con1.cursor()
            cursor1.execute("SELECT * FROM account WHERE name = %s AND email = %s AND password = %s",
                            (user, email_ac, passw))
            rows = cursor1.fetchall()
            if rows:
                MessageBox.showinfo("Status", "Successfully Logged In")
                if MessageBox.showinfo:
                    login_frame.pack_forget()
                    home_page()
            else:
                MessageBox.showinfo("Status", "Access Denied")

    show_ck = IntVar(value=0)

    def show_pass():
        if show_ck.get() == 1:
            password.config(show='')
        else:
            password.config(show='*')

    username = Entry(login_frame, font=('Roboto', 9), width=40, bd=0)
    email = Entry(login_frame, font=('Roboto', 9), width=40, bd=0)
    password = Entry(login_frame, show='*', font=('Roboto', 9), width=40, bd=0)
    log_ac = Button(login_frame, image=login_btn, command=login_acc, bd=0, bg='white')
    back_btn = Button(login_frame, image=back_button2, command=back_1, bd=0, bg='white')

    show_password = Checkbutton(login_frame, text="Show Password",
                                variable=show_ck, command=show_pass,
                                font=('arial', 9), offvalue=0, onvalue=1, bg='white')

    username.place(x=218, y=345)
    email.place(x=218, y=418)
    password.place(x=218, y=492)
    log_ac.place(x=205, y=560)
    back_btn.place(x=15, y=10)
    show_password.place(x=207, y=526)


def back_1():
    global sign_up_frame, login_frame
    try:
        sign_up_frame.pack_forget()
    except:
        pass
    try:
        login_frame.pack_forget()
    except:
        pass
    landing_frame.pack(side="top", expand=True, fill="both")


def home_page():
    global i, order_frame, history_frame, price, total_bal, user, back, j, price_label2
    global entry1, entry2, entry3, entry4, entry5, entry6, entry7, update_frame, email_ac
    global str_order_id, str_item_name, str_platform, str_quantity, str_date_ordered, str_date_arrival, flt_price

    landing_frame.pack_forget()

    home_frame = Frame(w, bg='#ffffff')
    home_frame.pack(side="top", expand=True, fill="both")

    canvas = Canvas(home_frame)
    canvas.pack(side="left", expand=True, fill="both")
    canvas.create_image(690, 386, image=bg)
    recents = Frame(canvas, width=200, height=100, bg='#ffffff')
    recents.place(x=630, y=485)

    def home():
        global price, total_bal, price_label, user, back, j, price_label2

        con2 = mysql.connect(host="localhost", user="root", password="admin01",
                             database="records")
        cursor2 = con2.cursor()
        price = cursor2.execute("SELECT SUM(price) FROM list WHERE email = '" + email_ac + "';")
        results = cursor2.fetchall()

        if results == [(None,)]:
            price_label = Label(home_frame, text='PHP 0000.00', font=('Bebas Neue', 55), justify='center', bg="#e9e9e6")
            price_label.place(x=362, y=280, anchor="center")
        else:
            total_bal = ["PHP"] + results
            try:
                price_label.place_forget()
                price_label2 = Label(home_frame, text='', font=('Bebas Neue', 55), justify='center',
                                     bg="#e9e9e6")
                price_label2.config(text=total_bal)
                price_label2.place(x=362, y=280, anchor="center")
            except NameError:
                price_label2 = Label(home_frame, text='', font=('Bebas Neue', 55), justify='center',
                                     bg="#e9e9e6")
                price_label2.config(text=total_bal)
                price_label2.place(x=362, y=280, anchor="center")

        con3 = mysql.connect(host="localhost", user="root", password="admin01",
                             database="records")
        cursor3 = con3.cursor()

        def logout():
            confirmation = MessageBox.askyesno("Log Out", "Do you want to log out your account?", icon='info',
                                               default='no')
            if confirmation:
                home_frame.pack_forget()
                landing_frame.pack(side="top", expand=True, fill="both")
            else:
                pass

        back = Button(home_frame, image=back_button2, command=logout, font=('arial', 10), bg='white', bd=0)
        back.place(x=28, y=110)

        def display():
            global i, j

            cursor3.execute("SELECT item_name, platform, date_arrival, price FROM records.list "
                            "WHERE email = '" + email_ac + "' ORDER BY date_arrival ASC LIMIT 4")
            results_my_cursor = cursor3.fetchall()

            for widget in recents.grid_slaves():
                widget.grid_forget()

            i = 0
            for x in results_my_cursor:  # Displaying The Table
                for j in range(len(x)):
                    e = Label(recents, width=24, text=x[j],
                              font=('roboto', 10), anchor="w", bg='#ffffff')
                    e.grid(row=i, column=j, padx=8, pady=20)
                i = i + 1

        display()

    home()

    def insert():
        global price_label, email_ac, price
        order_id = o_id.get()
        item_name = i_name.get()
        platform = s_platform.get()
        quantity = qty.get()
        date_ordered = d_ordered.get()
        date_arrival = d_arrive.get()
        price = cost.get()

        try:
            if ((order_id == "Order ID" or order_id == "") or (item_name == "" or item_name == "Item Name") or (
                    platform == "" or platform == "Shopping Platform") or
                    (quantity == "" or quantity == "Quantity") or (
                            date_ordered == "mm/dd/yy" or date_ordered == "") or (
                            date_arrival == "mm/dd/yy" or date_arrival == "") or
                    (price == "Price" or price == "")):

                MessageBox.showinfo("ALERT", "Please enter all fields")

            else:
                con1 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor1 = con1.cursor()

                # Check if order_id already exists for the given email
                cursor1.execute("SELECT order_id FROM list WHERE email = %s", (email_ac,))
                ids = cursor1.fetchall()

                if any(order_id == x[0] for x in ids):
                    MessageBox.showinfo("Status", "Cannot Have Duplicate IDs")
                else:
                    cursor1.execute("INSERT INTO list VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                                    (email_ac, order_id, item_name, platform, quantity, date_ordered, date_arrival,
                                     price))
                    con1.commit()
                    MessageBox.showinfo("Status", "Successfully Inserted")
                    con1.close()
                    home()
        except:
            MessageBox.showinfo("Status", "Input Error")

    def order_page():
        global order_frame, update_frame, back

        home_frame.pack_forget()

        order_frame = Frame(w, bg='#ffffff')
        order_frame.pack(side="top", expand=True, fill="both")

        order_canvas = Canvas(order_frame, bg='#ffffff')
        order_canvas.pack(side="left", expand=True, fill="both")

        order_canvas.create_image(680, 386, image=order_bg)

        back = Button(order_canvas, image=back_button, command=prev_page, font=('arial', 10), bg='#4d5967', bd=0)
        back.place(x=25, y=50)

        order_list = Frame(order_canvas, width=1360, height=10, bg='#ffffff')
        order_list.place(x=25, y=335)

        # scrollbar
        canvas_order = Canvas(order_list, width=1300, height=435, bg='#ffffff')
        canvas_order.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = Scrollbar(order_list, orient=VERTICAL, command=canvas_order.yview, bg='#ffffff')
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas_order.configure(yscrollcommand=scrollbar.set)
        canvas_order.bind('<Configure>', lambda e: canvas_order.configure(scrollregion=canvas_order.bbox("all")))
        order_frame_2 = Frame(canvas_order, bg='#ffffff')  # Frame window for all orders
        canvas_order.create_window((0, 0,), window=order_frame_2, anchor="nw")

        # will scroll when anywhere
        def _on_mousewheel(event):
            canvas_order.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas_order.bind_all("<MouseWheel>", _on_mousewheel)

        cb_1 = IntVar()
        cb_2 = IntVar()
        cb_3 = IntVar()
        cb_4 = IntVar()
        cb_5 = IntVar()

        def sort_arrival_asc():
            global i, j

            arrival_desc['state'] = "disabled"
            price_asc['state'] = "disabled"
            price_desc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_1.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.list WHERE email = '" + email_ac + "' ORDER BY date_arrival ASC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1
            else:
                arrival_desc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "' ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1

        def sort_arrival_desc():
            global i, j

            arrival_asc['state'] = "disabled"
            price_asc['state'] = "disabled"
            price_desc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_2.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "' ORDER BY date_arrival DESC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1
            else:
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1

        def sort_price_asc():
            global i, j

            price_desc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_3.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "' ORDER BY price ASC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1
            else:
                price_desc['state'] = "normal"
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1

        def sort_price_desc():
            global i, j

            price_asc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_4.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "' ORDER BY price DESC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1
            else:
                price_asc['state'] = "normal"
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                platform_group['state'] = "normal"
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1

        def group_platform():
            global i, j

            price_desc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            price_asc['state'] = "disabled"
            if cb_5.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "' ORDER BY platform ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1
            else:
                price_desc['state'] = "normal"
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal" \
                                     ""
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                                " FROM records.list WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in order_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(order_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5, pady=10)

                    edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)

                    i = i + 1

        arrival_asc = Checkbutton(order_frame, text="Asc", variable=cb_1, command=sort_arrival_asc, onvalue=1,
                                  offvalue=0,
                                  font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        arrival_desc = Checkbutton(order_frame, text="Dsc", variable=cb_2, command=sort_arrival_desc, onvalue=1,
                                   offvalue=0,
                                   font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        price_asc = Checkbutton(order_frame, text="Asc", variable=cb_3, command=sort_price_asc, onvalue=1, offvalue=0,
                                font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        price_desc = Checkbutton(order_frame, text="Dsc", variable=cb_4, command=sort_price_desc, onvalue=1, offvalue=0,
                                 font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        platform_group = Checkbutton(order_frame, text="Platform", variable=cb_5, command=group_platform,
                                     onvalue=1, offvalue=0, font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')

        arrival_asc.place(x=810, y=133)
        arrival_desc.place(x=811, y=153)
        price_asc.place(x=950, y=133)
        price_desc.place(x=951, y=153)
        platform_group.place(x=1050, y=133)

        def search():
            global i, j
            con6 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor6 = con6.cursor()
            cursor6.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                            " FROM records.list WHERE order_id= '" + search_box.get() + "' "
                                                                                        "and email = '" + email_ac + "'")
            results_my_cursor_3 = cursor6.fetchall()

            if results_my_cursor_3:
                i = 0
                for x in results_my_cursor_3:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(select_frame, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=5)

                    edit_bt = Button(select_frame, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                     command=lambda k=x[0]: edit_data(k))
                    delete_bt = Button(select_frame, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_data(k))
                    delete_bt.grid(row=i, column=9, padx=10)
                    edit_bt.grid(row=i, column=8, padx=10)
                i = i + 1
            else:
                MessageBox.showinfo("Status", "There are no ID names that match: " + search_box.get())

            update_frame.place_forget()
            select_frame.place(x=30, y=260)

        update_frame = Frame(order_frame, width=1300, height=20, bg='#ffffff')  # Frame will appear for updating
        update_frame.place(x=40, y=260)
        select_frame = Frame(order_frame, width=1300, height=20, bg='#ffffff')
        select_frame.place(x=30, y=260)

        search_box = Entry(order_frame, font=('roboto', 10), width=40, bd=0)
        search_box.insert(0, "Search ID")
        search_box.place(x=138, y=135)
        search_button = Button(order_frame, image=search_btn, command=search, bd=0, bg='#ffffff')
        search_button.place(x=565, y=128)

        def display_order():
            global i, j
            con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor4 = con4.cursor()

            cursor4.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                            " FROM records.list WHERE email = '" + email_ac + "'")
            results_my_cursor_2 = cursor4.fetchall()

            # Clear existing widgets
            for widget in order_frame_2.grid_slaves():
                widget.grid_forget()

            i = 0
            for x in results_my_cursor_2:  # Displaying The Table
                for j in range(len(x)):
                    items = Label(order_frame_2, width=22, text=x[j], font=('roboto', 9), anchor="w", bg='#ffffff')
                    items.grid(row=i, column=j, padx=5, pady=10)

                edit_bt = Button(order_frame_2, image=edit_button, bg='#ffffff', bd=0, anchor="center",
                                 command=lambda k=x[0]: edit_data(k))
                delete_bt = Button(order_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                   command=lambda k=x[0]: delete_data(k))
                delete_bt.grid(row=i, column=9, padx=10)
                edit_bt.grid(row=i, column=8, padx=10)

                i = i + 1

        display_order()

        def delete_data(order_id):
            global email_ac
            con5 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor5 = con5.cursor()
            my_var = MessageBox.askyesnocancel("Delete", "Delete ORDER: " + str(order_id), icon='warning',
                                               default='no')
            if my_var:  # True if yes button is clicked
                cursor5.execute(
                    "INSERT INTO records.history "
                    "(email, item_name, platform, quantity, date_ordered, date_arrival, price) "
                    "SELECT email, item_name, platform, quantity, date_ordered, date_arrival, price FROM records.list "
                    "WHERE email = '" + email_ac + "' and order_id=" + str(order_id))
                cursor5.execute("DELETE FROM records.list "
                                "WHERE email = '" + email_ac + "' and order_id=" + str(order_id))
                cursor5.execute("commit")
                con5.close()

            display_order()
            price_label2.place_forget()
            select_frame.place_forget()

        def edit_data(order_id):
            global i, entry1, entry2, entry3, entry4, entry5, entry6, entry7, str_quantity, str_date_ordered
            global str_order_id, str_item_name, str_platform, str_date_arrival, flt_price

            mydb = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            mycursor = mydb.cursor()
            mycursor.execute("SELECT order_id, item_name, platform, quantity, date_ordered, date_arrival, price"
                             " FROM records.list WHERE email = '" + email_ac + "' and order_id=" + order_id)
            s = mycursor.fetchone()  # row details as tuple

            str_order_id = StringVar(w)  # String variable
            str_item_name = StringVar(w)
            str_platform = StringVar(w)
            str_quantity = StringVar(w)
            str_date_ordered = StringVar(w)
            str_date_arrival = StringVar(w)
            flt_price = DoubleVar(w)

            str_order_id.set(s[0])
            str_item_name.set(s[1])
            str_platform.set(s[2])
            str_quantity.set(s[3])
            str_date_ordered.set(s[4])
            str_date_arrival.set(s[5])
            flt_price.set(s[6])

            entry1 = Entry(update_frame, textvariable=str_order_id, font=('arial', 9), width=22, state='disabled', bd=0)
            entry1.grid(row=0, column=0, padx=6)
            entry2 = Entry(update_frame, textvariable=str_item_name, font=('arial', 9), width=22, bd=0)
            entry2.grid(row=0, column=1, padx=6)
            entry3 = Entry(update_frame, textvariable=str_platform, font=('arial', 9), width=22, bd=0)
            entry3.grid(row=0, column=2, padx=6)
            entry4 = Entry(update_frame, textvariable=str_quantity, font=('arial', 9), width=22, bd=0)
            entry4.grid(row=0, column=3, padx=6)
            entry5 = Entry(update_frame, textvariable=str_date_ordered, font=('arial', 9), width=22, bd=0)
            entry5.grid(row=0, column=4, padx=6)
            entry6 = Entry(update_frame, textvariable=str_date_arrival, font=('arial', 9), width=22, bd=0)
            entry6.grid(row=0, column=5, padx=6)
            entry7 = Entry(update_frame, textvariable=flt_price, font=('arial', 9), width=22, bd=0)
            entry7.grid(row=0, column=6, padx=6)

            update_bt = Button(update_frame, image=update_button, command=lambda: update_data(), anchor="w", bd=0,
                               bg='#ffffff')
            update_bt.grid(row=0, column=8, padx=20)
            cancel_update_bt = Button(update_frame, image=cancel_button, command=lambda: cancel_update(),
                                      anchor="w", bd=0, bg='#ffffff')
            cancel_update_bt.grid(row=0, column=9, padx=15)

            select_frame.place_forget()
            update_frame.place(x=30, y=260)

        def cancel_update():
            update_frame.place_forget()

        def update_data():  # update record
            global entry1, entry2, entry3, entry4, entry5, entry6, entry7, update_frame, flt_price
            global str_order_id, str_item_name, str_platform, str_quantity, str_date_ordered, str_date_arrival

            mydb2 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            mycursor2 = mydb2.cursor()

            data = (str_item_name.get(), str_platform.get(), str_quantity.get(), str_date_ordered.get(),
                    str_date_arrival.get(), flt_price.get(), str_order_id.get())
            mycursor2.execute("UPDATE records.list SET item_name=%s,platform=%s,\
                               quantity=%s,date_ordered=%s, date_arrival=%s, price=%s "
                              "WHERE email = '" + email_ac + "' and order_id = %s", data)

            mycursor2.execute("commit")
            mydb2.close()
            MessageBox.showinfo("Status", "Successfully Updated")
            update_frame.place_forget()
            price_label2.place_forget()
            display_order()  # refresh the data

    def history_page():
        global history_frame, email_ac, back

        home_frame.pack_forget()

        history_frame = Frame(w, bg='#ffffff')
        history_frame.pack(side="top", expand=True, fill="both")

        history_canvas = Canvas(history_frame, bg='#ffffff')
        history_canvas.pack(side="left", expand=True, fill="both")

        history_canvas.create_image(680, 386, image=history_bg)

        back = Button(history_canvas, image=back_button, command=prev_page, font=('arial', 10), bg='#4d5967', bd=0)
        back.place(x=25, y=50)

        history_list = Frame(history_frame, width=1360, height=600, bg='#ffffff')
        history_list.place(x=22, y=325)

        # scrollbar
        canvas_history = Canvas(history_list, width=1300, height=450, bg='#ffffff')
        canvas_history.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar = Scrollbar(history_list, orient=VERTICAL, command=canvas_history.yview, bg='#ffffff')
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas_history.configure(yscrollcommand=scrollbar.set)
        canvas_history.bind('<Configure>', lambda e: canvas_history.configure(scrollregion=canvas_history.bbox("all")))
        history_frame_2 = Frame(canvas_history, bg='#ffffff')  # Frame window for all orders
        canvas_history.create_window((0, 0,), window=history_frame_2, anchor="nw")

        # will scroll when anywhere
        def _on_mousewheel(event):
            canvas_history.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas_history.bind_all("<MouseWheel>", _on_mousewheel)

        cb_1 = IntVar()
        cb_2 = IntVar()
        cb_3 = IntVar()
        cb_4 = IntVar()
        cb_5 = IntVar()

        def sort_arrival_asc():
            global i, j

            arrival_desc['state'] = "disabled"
            price_asc['state'] = "disabled"
            price_desc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_1.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute(
                    "SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                    "FROM records.history WHERE email = '" + email_ac + "' ORDER BY date_arrival ASC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1
            else:
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1

        def sort_arrival_desc():
            global i, j

            arrival_asc['state'] = "disabled"
            price_asc['state'] = "disabled"
            price_desc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_2.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute(
                    "SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                    "FROM records.history WHERE email = '" + email_ac + "' ORDER BY date_arrival DESC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1
            else:
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1

        def sort_price_asc():
            global i, j

            price_desc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_3.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "' ORDER BY price ASC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1
            else:
                arrival_asc['state'] = "normal"
                arrival_desc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1

        def sort_price_desc():
            global i, j

            price_asc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            platform_group['state'] = "disabled"

            if cb_4.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "' ORDER BY price DESC ")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1
            else:
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1

        def group_platform():
            global i, j

            price_asc['state'] = "disabled"
            arrival_desc['state'] = "disabled"
            arrival_asc['state'] = "disabled"
            price_desc['state'] = "disabled"

            if cb_5.get() == 1:
                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "' ORDER BY platform")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1
            else:
                arrival_desc['state'] = "normal"
                arrival_asc['state'] = "normal"
                price_asc['state'] = "normal"
                price_desc['state'] = "normal"
                platform_group['state'] = "normal"

                con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
                cursor4 = con4.cursor()

                cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                                "FROM records.history WHERE email = '" + email_ac + "'")
                results_my_cursor_2 = cursor4.fetchall()

                for widget in history_frame_2.grid_slaves():
                    widget.grid_forget()

                i = 0
                for x in results_my_cursor_2:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(history_frame_2, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    delete_bt.grid(row=i, column=9, padx=3)
                    i = i + 1

        arrival_asc = Checkbutton(history_frame, text="Asc", variable=cb_1, command=sort_arrival_asc, onvalue=1,
                                  offvalue=0,
                                  font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        arrival_desc = Checkbutton(history_frame, text="Dsc", variable=cb_2, command=sort_arrival_desc, onvalue=1,
                                   offvalue=0,
                                   font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        price_asc = Checkbutton(history_frame, text="Asc", variable=cb_3, command=sort_price_asc, onvalue=1, offvalue=0,
                                font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        price_desc = Checkbutton(history_frame, text="Dsc", variable=cb_4, command=sort_price_desc, onvalue=1,
                                 offvalue=0,
                                 font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')
        platform_group = Checkbutton(history_frame, text="Platform", variable=cb_5, command=group_platform,
                                     onvalue=1, offvalue=0, font=('arial', 7), width=5, bd=0, bg='#263546', fg='white')

        arrival_asc.place(x=810, y=133)
        arrival_desc.place(x=811, y=153)
        price_asc.place(x=950, y=133)
        price_desc.place(x=951, y=153)
        platform_group.place(x=1050, y=133)

        def search():
            global i, j
            search_data = search_box.get()
            con6 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor6 = con6.cursor()
            cursor6.execute(
                "SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                "FROM records.history WHERE email = '" + email_ac + "'and item_name "
                                                                    "LIKE CONCAT ('%', '" + search_data + "', '%')")
            results_my_cursor_3 = cursor6.fetchall()

            if results_my_cursor_3:
                i = 0
                for x in results_my_cursor_3:  # Displaying The Table
                    for j in range(len(x)):
                        items = Label(select_frame, width=22, text=x[j],
                                      font=('roboto', 9), anchor="w", bg='#ffffff')
                        items.grid(row=i, column=j, padx=20, pady=10)
                    delete_bt = Button(select_frame, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: delete_history(k))
                    cancel_bt = Button(select_frame, image=cancel_button, bg='#ffffff', bd=0, anchor="center",
                                       command=lambda k=x[0]: cancel_select())
                    delete_bt.grid(row=i, column=9, padx=10)
                    cancel_bt.grid(row=i, column=10, padx=10)
                i = i + 1
            else:
                MessageBox.showinfo("Status", "There are no ID names that match: " + search_box.get())

            select_frame.place(x=30, y=260)

        select_frame = Frame(history_frame, width=1300, height=20, bg='#ffffff')
        select_frame.place(x=30, y=260)

        search_box = Entry(history_frame, font=('roboto', 10), width=40, bd=0)
        search_box.insert(0, "Search Item Name")
        search_box.place(x=138, y=135)
        search_button = Button(history_frame, image=search_btn, command=search, bd=0, bg='#ffffff')
        search_button.place(x=565, y=128)

        def cancel_select():
            select_frame.place_forget()

        def display_history():
            global i, j
            con4 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor4 = con4.cursor()

            cursor4.execute("SELECT item_name, platform, quantity, date_ordered, date_arrival, price "
                            "FROM records.history WHERE email = '" + email_ac + "' ")
            results_my_cursor_2 = cursor4.fetchall()

            for widget in history_frame_2.grid_slaves():
                widget.grid_forget()

            i = 0
            for x in results_my_cursor_2:  # Displaying The Table
                for j in range(len(x)):
                    items = Label(history_frame_2, width=22, text=x[j],
                                  font=('roboto', 9), anchor="w", bg='#ffffff')
                    items.grid(row=i, column=j, padx=20, pady=10)
                delete_bt = Button(history_frame_2, image=delete_button, bg='#ffffff', bd=0, anchor="center",
                                   command=lambda k=x[0]: delete_history(k))
                delete_bt.grid(row=i, column=9, padx=3)
                i = i + 1

        display_history()

        def delete_history(item_name):
            con7 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor7 = con7.cursor()
            my_var2 = MessageBox.askyesnocancel("Delete ?", "Delete ORDER: " + str(item_name), icon='warning',
                                                default='no')
            if my_var2:  # True if yes button is clicked
                cursor7.execute("DELETE FROM records.history "
                                "WHERE email = %s AND item_name = %s", (email_ac, item_name))
                cursor7.execute("commit")
                con7.close()
                display_history()

        def clear_history():
            con7 = mysql.connect(host="localhost", user="root", password="admin01", database="records")
            cursor7 = con7.cursor()
            my_var2 = MessageBox.askyesnocancel("Clear History", "Are you sure to clear history?", icon='warning',
                                                default='no')
            if my_var2:  # True if yes button is clicked
                cursor7.execute("DELETE FROM records.history WHERE email = '" + email_ac + "'")
                cursor7.execute("commit")
                con7.close()
                display_history()

            display_history()

        clear_history_button = Button(history_frame, image=clear_history_btn, command=clear_history, font=('arial', 10),
                                      bd=0, bg='#263546')
        clear_history_button.place(x=820, y=180)

    def prev_page():
        global order_frame, history_frame

        try:
            order_frame.pack_forget()
        except:
            pass
        try:
            history_frame.pack_forget()
        except:
            pass

        home_frame.pack(side="top", expand=True, fill="both")
        home()

    def close_page():
        w.quit()

    welcome_text = str('Heads up ' + user + '! Your orders might be arriving soon.')
    o_id = Entry(home_frame, font=('arial', 9), width=50, bd=0)
    i_name = Entry(home_frame, font=('arial', 9), width=50, bd=0)
    s_platform = Entry(home_frame, font=('arial', 9), width=25, bd=0)
    qty = Entry(home_frame, font=('arial', 9), width=10, bd=0)
    d_ordered = Entry(home_frame, font=('arial', 9), width=15, bd=0)
    d_arrive = Entry(home_frame, font=('arial', 9), width=15, bd=0)
    cost = Entry(home_frame, font=('arial', 9), width=50, bd=0)
    welcome = Label(home_frame, text=welcome_text, font=('roboto black', 11), fg='#252525', bg='white')

    add_order = Button(home_frame, image=button_add, command=insert, bd=0)
    orders = Button(home_frame, image=orders_button, command=order_page, font=('arial', 10), bd=0, bg="#3a4d5b")
    history = Button(home_frame, image=history_button, command=history_page, font=('arial', 10), bd=0, bg="#3a4d5b")
    close = Button(home_frame, image=close_button, command=close_page, bd=0, bg="#3a4d5b")

    o_id.insert(0, "Order ID")
    i_name.insert(0, "Item Name")
    s_platform.insert(0, "Shopping Platform")
    qty.insert(0, "Quantity")
    d_ordered.insert(0, "mm/dd/yy")
    d_arrive.insert(0, "mm/dd/yy")
    cost.insert(0, "Price")

    o_id.place(x=185, y=437)
    i_name.place(x=185, y=481)
    s_platform.place(x=185, y=525)
    qty.place(x=435, y=525)
    d_ordered.place(x=185, y=592)
    d_arrive.place(x=380, y=592)
    cost.place(x=185, y=637)
    add_order.place(x=174, y=680)
    orders.place(x=695, y=80)
    history.place(x=980, y=80)
    close.place(x=1320, y=10)
    welcome.place(x=615, y=375)


login_bt = Button(landing_frame, image=login, command=login_page, font=('arial', 10), bd=0, bg="#263546")
login_bt.place(x=990, y=320)
sign_up_bt = Button(landing_frame, image=sign_up, command=create_account, font=('arial', 10), bd=0, bg="#263546")
sign_up_bt.place(x=990, y=420)

w.mainloop()
