import datetime
import os
import sqlite3
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

# .......................... Reports .......................
db_name = os.path.splitext(os.path.basename(__file__))[0] + 'db'
#
#
def b_connect():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'create table if not exists category (cat_id INTEGER PRIMARY KEY, cat_name VARCHAR NOT NULL, created_at DATE '
        'NOT NULL, '
        'updated_at DATE NOT NULL)')
    cur.execute(
        'create table if not exists book (book_id INTEGER PRIMARY KEY, title VARCHAR NOT NULL, author VARCHAR NOT '
        'NULL, book_year INTEGER NOT NULL, isbn varchar NOT NULL, book_count integer NOT '
        'NULL, created_at DATE NOT NULL, updated_at DATE NOT NULL, cat_id INTEGER NOT NULL, FOREIGN KEY(cat_id) '
        'REFERENCES '
        'category(cat_id))')
    cur.execute(
        'create table if not exists user (user_id INTEGER PRIMARY KEY, user_name VARCHAR NOT NULL, '
        'user_family VARCHAR NOT NULL, user_age INTEGER NOT NULL, user_phone INTEGER NOT NULL, mail varchar, '
        'created_at DATE NOT NULL, updated_at '
        'DATE NOT NULL)')
    cur.execute(
        'create table if not exists logs (log_id INTEGER PRIMARY KEY, status VARCHAR, log_type VARCHAR, '
        'description VARCHAR, fail_description VARCHAR, created_at DATE)')
    cur.execute(
        'create table if not exists reserve (reserve_id INTEGER PRIMARY KEY, user_id VARCHAR NOT NULL, '
        'book_id VARCHAR NOT NULL, count INTEGER NOT NULL, status VARCHAR NOT NULL, duration INTEGER NOT '
        'NULL, created_at DATE NOT NULL)')
    connection.commit()
    connection.close()


def b_count_books():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert Book' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_users():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert User' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_del():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Delete Book' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_category():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert Category' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


# .......................... Basic Settings .......................
home = Tk()
home.title('Library')
home.geometry('900x480')
home.resizable(width=False, height=False)
font1 = ("Comic Sans MS", 13, "bold")
font2 = ("Comic Sans MS", 10)
books_num = IntVar()
users_num = IntVar()
dels_num = IntVar()
cat_num = IntVar()

# .......................... Trees .......................
s = ttk.Style()
s.theme_use('clam')
tree_book = ttk.Treeview(home, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"), show='headings', height=7)
tree_book.column("#1", anchor=CENTER, width=7)
tree_book.heading("# 1", text="ID")
tree_book.column("# 2", anchor=CENTER, width=170)
tree_book.heading("# 2", text="Title")
tree_book.column("# 3", anchor=CENTER, width=160)
tree_book.heading("# 3", text="Author")
tree_book.column("# 4", anchor=CENTER, width=100)
tree_book.heading("# 4", text="Category")
tree_book.column("# 5", anchor=CENTER, width=50)
tree_book.heading("# 5", text="Year")
tree_book.column("# 6", anchor=CENTER, width=80)
tree_book.heading("# 6", text="ISBN")
tree_book.column("# 7", anchor=CENTER, width=55)
tree_book.heading("# 7", text="Count")
tree_book.column("# 8", anchor=CENTER, width=130)
tree_book.heading("# 8", text="Created At")
tree_book.column("# 9", anchor=CENTER, width=130)
tree_book.heading("# 9", text="Updated At")
tree_book.grid(row=3, column=0, padx=5, pady=5, columnspan=4)

tree_user = ttk.Treeview(home, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings', height=7)
tree_user.column("#1", anchor=CENTER, width=7)
tree_user.heading("# 1", text="ID")
tree_user.column("# 2", anchor=CENTER, width=90)
tree_user.heading("# 2", text="Name")
tree_user.column("# 3", anchor=CENTER, width=110)
tree_user.heading("# 3", text="Family")
tree_user.column("# 4", anchor=CENTER, width=40)
tree_user.heading("# 4", text="Age")
tree_user.column("# 5", anchor=CENTER, width=85)
tree_user.heading("# 5", text="Phone")
tree_user.column("# 6", anchor=CENTER, width=195)
tree_user.heading("# 6", text="Mail")
tree_user.column("# 7", anchor=CENTER, width=130)
tree_user.heading("# 7", text="Created At")
tree_user.column("# 8", anchor=CENTER, width=130)
tree_user.heading("# 8", text="Updated At")
tree_user.grid(row=4, column=0, padx=5, pady=5, columnspan=4)

# canvas = Canvas(home, width=256, height=256)
# canvas.grid(row=0,column=5, columnspan=4)
# img = PhotoImage(file='img/100.png')
# canvas.create_image(20, 20, anchor=NW, image=img)

# .......................... Menu Items .......................
topMenu = Menu(home)
bookmenu = Menu(topMenu, tearoff=False)
bookmenu.add_command(label='Search Book', command=lambda: search_book_window())
bookmenu.add_command(label='Add Book', command=lambda: add_book_window())
bookmenu.add_command(label='Delete Book', command=lambda: delete_book_window())
bookmenu.add_command(label='Add Category', command=lambda: add_category_window())
bookmenu.add_command(label='Update Book', command=lambda: update_book_window())
bookmenu.add_command(label='Exit', command=home.quit)
topMenu.add_cascade(label='Books', menu=bookmenu)

usermenu = Menu(home, tearoff=False)
usermenu.add_command(label='Search User', command=lambda: nothing())
usermenu.add_command(label='Add User', command=lambda: add_user_view())
usermenu.add_command(label='Delete User', command=lambda: nothing())
usermenu.add_command(label='Update User', command=lambda: nothing())
topMenu.add_cascade(label='Users', menu=usermenu)

othermenu = Menu(home, tearoff=False)
othermenu.add_command(label='Search Logs', command=lambda: logs_window())
othermenu.add_command(label='DB Tools', command=lambda: db_tools_window())
bookmenu.add_separator()
othermenu.add_command(label='Help', command=lambda: nothing())
topMenu.add_cascade(label='Others', menu=othermenu)

report = Button(home, text='Report', command=lambda: report_home(), width=10)
report.grid(row=0, column=0, pady=5)
refresh = Button(home, text='Refresh', command=lambda: view_all_home(), width=10)
refresh.grid(row=0, column=1, pady=5)
book_view = Button(home, text='Book View', command=lambda: view_a_book(), width=10)
book_view.grid(row=0, column=2, pady=5)
user_view = Button(home, text='user View', command=lambda: view_a_user(), width=10)
user_view.grid(row=0, column=3, pady=5)

booksCount = Label(home, textvariable=books_num)
booksCount.grid(row=1, column=0, pady=5)
booksCount.configure(font=font2)
text2 = Label(home, text='Books')
text2.grid(row=2, column=0)
text2.configure(font=font2)

booksDeleted = Label(home, textvariable=dels_num)
booksDeleted.grid(row=1, column=1, pady=5)
booksDeleted.configure(font=font2)
text3 = Label(home, text='Deletes')
text3.grid(row=2, column=1, pady=5)
text3.configure(font=font2)

userCount = Label(home, textvariable=users_num)
userCount.grid(row=1, column=2, pady=5)
userCount.configure(font=font2)
text4 = Label(home, text='Users')
text4.grid(row=2, column=2)
text4.configure(font=font2)

reservCount = Label(home, textvariable=cat_num)
reservCount.grid(row=1, column=3, pady=5)
reservCount.configure(font=font2)
text5 = Label(home, text='Categories')
text5.grid(row=2, column=3)
text5.configure(font=font2)


# .......................... DB Functions .......................
def b_insert_log(status, log_type, desc, fail_desc):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into logs values (NULL, ?,?,?,?,?)',
                (status, log_type, desc, fail_desc, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_add_user(name, family, age, phone, mail):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into user values (NULL, ?,?,?,?,?,?,?)',
                (name, family, age, phone, mail, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_add_book(title, author, book_year, isbn, book_count, cat_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into book values (NULL, ?,?,?,?,?,?,?,?)',
                (title, author, book_year, isbn, book_count,
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cat_id))
    connection.commit()
    connection.close()


def b_add_category(name):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into category values (NULL, ?,?,?)',
                (name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_update_book(book_id, title, author, cat_id, book_year, isbn, book_count):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('update book set title=?, author=?, cat_id=?, book_year=?, isbn=?, '
                'book_count=?, updated_at=? where book_id=?',
                (title, author, cat_id, book_year, isbn, book_count,
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 book_id))
    connection.commit()
    connection.close()


def b_search_logs(log_status='', log_type='', log_desc='', log_faildesc='', created_at=''):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select * from logs where status like ? and log_type like ? and '
        'description like ? and  fail_description like ? and created_at like ?',
        ('%' + log_status + '%', '%' + log_type + '%', '%' + log_desc + '%',
         '%' + log_faildesc + '%', '%' + created_at + '%'))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_search_book_or(title='', author='', cat_id='', book_year='', isbn='', book_count=''):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book where title like ? or author like ? or cat_id like ? or '
        'book_year like ? or isbn like ? or '
        'book_count like ?', (title, author, cat_id, book_year, isbn, book_count))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_search_book_and(title=None, author=None, cat_id=None, book_year=None, isbn=None, book_count=None):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book where title=coalesce(?,title) and '
        'author=coalesce(?,author) and cat_id=coalesce(?,cat_id) and book_year=coalesce(?,book_year) and '
        'isbn=coalesce(?,isbn) and book_count=coalesce(?,book_count)',
        (title, author, cat_id, book_year, isbn, book_count))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_del_book(book_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from book where book_id=?', (book_id,))
    connection.commit()
    connection.close()


def b_view_all_book():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book order by book_id desc')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_view_all_cat():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select cat_id, cat_name, created_at, updated_at '
        'from category order by cat_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_view_all_user():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('select * from user order by user_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_view_all_logs():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('select * from logs order by log_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_del_log(log_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from logs where log_id=?', (log_id,))
    connection.commit()
    connection.close()


def b_logs_drop():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from logs')
    connection.commit()
    connection.close()


def b_delete_db():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from user')
    cur.execute('delete from book')
    cur.execute('delete from category')
    cur.execute('delete from logs')
    cur.execute('delete from reserve')
    connection.commit()
    connection.close()


def b_import_data():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sqluser = [
        ('Hossein', 'Rezaeizadeh', 22, '9391234321', 'h.rezaeizadeh@gmail.com', '2022-02-12 22:12:40',
         '2022-04-15 10:14:26'),
        ('Saeed', 'Ghasemi', 27, '9309876543', 'saeedghasemi1372@gmail.com', '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Karim', 'Benzema', 34, '9122105271', 'karimbenzema@gmail.com', '2020-05-05 10:20:46',
         '2020-05-05 10:04:26'),
        ('Saeed', 'Mohammadi', 34, '9356706868', 'mohammadisaeedir@gmail.com', '2022-03-12 13:00:46',
         '2022-03-11 13:04:26'),
        ('Zeinab', 'Rezaeizadeh', 33, '9364637883', 'z3inab.rezaei@gmail.com', '2022-05-22 13:01:46',
         '2022-04-21 00:24:26')
    ]
    stmt = "insert into user (user_name, user_family, user_age, user_phone, mail, created_at, updated_at) " \
           "values (?, ?, ?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqluser)
    sqlbook = [
        ('Strategy', 'Engolo Cante', 4, 1987, 'L23451', 2500, '2022-02-12 22:12:40',
         '2022-04-15 10:14:26'),
        ('Knowledge', 'Fede Valverde', 2, 1990, 'S23452', 3000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Python', 'Simon Kayer', 1, 1991, 'M21343', 1000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Django', 'Saeed Rezaei', 3, 2010, 'K12345', 8000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Real Madrid', 'Sergio Ramoos', 1, 1989, 'V23452', 3500, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10')
    ]
    stmt = "insert into book (title, author, cat_id, book_year, isbn, book_count, created_at, updated_at) " \
           "values (?, ?, ?, ?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqlbook)
    sqlcategory = [
        ('History', '2022-05-02 22:12:40', '2022-14-15 11:34:26'),
        ('Science', '2020-12-11 22:12:40', '2022-08-15 10:24:26'),
        ('Sport', '2021-02-03 22:12:40', '2022-04-15 20:17:26'),
        ('Programing', '2022-02-12 22:12:40', '2022-14-15 12:14:26')
    ]
    stmt = "insert into category (cat_name, created_at, updated_at) values (?, ?, ?)"
    cur.executemany(stmt, sqlcategory)
    sqllogs = [
        ('Success', 'Insert User', 'Saeed Mohammadi is added', '-', '2022-22-12 10:55:26'),
        ('Failure', 'Delete User', 'User id: 1 is deleted', 'ConnectioError', '2022-14-10 11:24:16'),
        ('Success', 'Insert User', 'Zeinab Rezaeizadeh is added', '-', '2022-13-08 17:11:36'),
        ('Failure', 'Delete Book', 'Book Id: 6 is deleted', 'TclError', '2022-21-07 11:22:44'),
        ('Success', 'Delete Book', 'Book Id: 8 is deleted', '-', '2022-21-07 11:22:44'),
        ('Success', 'Insert Book', 'Strategy by Engolo Cante is added', '-', '2022-06-01 21:54:46'),
        ('Success', 'Insert Book', 'Knowledge by Fede Valverde is added', '-', '2022-06-01 21:54:46'),
        ('Success', 'Insert Category', 'The Category: Sport is added', '-', '2021-06-01 21:54:46'),
        ('Success', 'Update Book', 'Python by Simon Kayer is Updated', '-', '2021-12-04 00:10:41'),
        ('Failure', 'Update User', 'Saeed Mohammadi is Updated', 'TclError', '2021-11-04 04:50:49'),
        ('Success', 'Insert Book', 'Flask by Python Developer is added', '-', '2021-10-02 15:40:43'),
        ('Success', 'Insert Book', 'Python by Simon Kayer is added', '-', '2021-10-02 15:40:43')
    ]
    stmt = "insert into logs (status, log_type, description, fail_description, created_at) " \
           "values (?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqllogs)
    connection.commit()
    connection.close()


def b_view_list_cat():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select distinct cat_name, cat_id '
        'from category group by cat_name order by cat_name')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


# .......................... Main Page Functions .......................

def view_a_book():
    try:
        index = tree_book.focus()
        tkinter.messagebox.showinfo('Book Information', f'Book ID:    {tree_book.item(index)["values"][0]}\n'
                                                        f'Title:    {tree_book.item(index)["values"][1]}\n'
                                                        f'Author:   {tree_book.item(index)["values"][2]}\n'
                                                        f'Category:   {tree_book.item(index)["values"][3]}\n'
                                                        f'Book Year:    {tree_book.item(index)["values"][4]}\n'
                                                        f'ISBN:    {tree_book.item(index)["values"][5]}\n'
                                                        f'Book Count:   {tree_book.item(index)["values"][6]}\n'
                                                        f'Created At:   {tree_book.item(index)["values"][7]}\n'
                                                        f'Updated At:   {tree_book.item(index)["values"][8]}')
    except IndexError:
        tkinter.messagebox.showerror('Error', 'No item is Selected')


def view_a_user():
    try:
        index = tree_user.focus()
        tkinter.messagebox.showinfo('User Information', f'User ID:    {tree_user.item(index)["values"][0]}\n'
                                                        f'Name:    {tree_user.item(index)["values"][1]}\n'
                                                        f'Family:   {tree_user.item(index)["values"][2]}\n'
                                                        f'Age:    {tree_user.item(index)["values"][3]}\n'
                                                        f'Phone:    (+98)-{tree_user.item(index)["values"][4]}\n'
                                                        f'Email:   {tree_user.item(index)["values"][5]}\n'
                                                        f'Created At:   {tree_user.item(index)["values"][6]}\n'
                                                        f'Updated At:   {tree_user.item(index)["values"][7]}')
    except IndexError:
        tkinter.messagebox.showerror('Error', 'No item is Selected')


def view_all_home():
    try:
        for i in tree_book.get_children():
            tree_book.delete(i)
        books = b_view_all_book()
        for item in books:
            tree_book.insert('', 'end', values=item)
        for i in tree_user.get_children():
            tree_user.delete(i)
        users = b_view_all_user()
        for item in users:
            tree_user.insert('', 'end', values=item)
    except ConnectionError:
        b_insert_log('Failure', 'View All Tree', 'Could not retrieve all Data from user or book table',
                     'ConnectionError')
        tkinter.messagebox.showerror('ConnectionError', 'Database is not available')


def nothing():
    pass


def report_home():
    books_num.set(b_count_books())
    users_num.set(b_count_users())
    dels_num.set(b_count_del())
    cat_num.set(b_count_category())


def cat_List_id():
    cat_list = dict(b_view_list_cat())
    value_list = []
    for value in cat_list.keys():
        value_list.append(value)
    return value_list


# .......................... Windows .......................

def add_user_view():
    adduser = Toplevel(home)
    adduser.title('Add User')
    adduser.geometry('260x260')
    adduser.resizable(width=False, height=False)
    user_name = StringVar()
    user_family = StringVar()
    user_age = IntVar(value='')
    user_phone = IntVar(value='')
    user_mail = StringVar()

    # ------------------------ add form --------------------
    text6 = Label(adduser, text='Add New User')
    text6.grid(row=0, column=0, columnspan=2, pady=10)
    text6.configure(font=font2)

    titleLabel = Label(adduser, text='Name:* ')
    titleLabel.grid(row=1, column=0, pady=5, padx=5)
    titleEntry = Entry(adduser, textvariable=user_name, width=30)
    titleEntry.grid(row=1, column=1, pady=5, padx=5)

    authorLabel = Label(adduser, text='Family:* ')
    authorLabel.grid(row=2, column=0, pady=5, padx=5)
    authorEntry = Entry(adduser, textvariable=user_family, width=30)
    authorEntry.grid(row=2, column=1, pady=5, padx=5)

    book_yearLabel = Label(adduser, text='Age:* ')
    book_yearLabel.grid(row=3, column=0, pady=5, padx=5)
    book_yearEntry = Entry(adduser, textvariable=user_age, width=30)
    book_yearEntry.grid(row=3, column=1, pady=5, padx=5)

    isbnLabel = Label(adduser, text='Phone:* ')
    isbnLabel.grid(row=4, column=0, pady=5, padx=5)
    isbnEntry = Entry(adduser, textvariable=user_phone, width=30)
    isbnEntry.grid(row=4, column=1, pady=5, padx=5)

    book_countLabel = Label(adduser, text='Email: ')
    book_countLabel.grid(row=5, column=0, pady=5, padx=5)
    book_countEntry = Entry(adduser, textvariable=user_mail, width=30)
    book_countEntry.grid(row=5, column=1, pady=5, padx=5)

    submit = Button(adduser, text='Insert User', width=20,
                    command=lambda: add_user(), bg='#217C7E', fg='White')
    submit.grid(row=6, column=0, columnspan=2)

    # ------------------------ add form --------------------
    def add_user():
        try:
            if user_name.get() and user_family.get() and user_age.get() and user_phone.get():
                b_add_user(user_name.get(), user_family.get(), user_age.get(), user_phone.get(), user_mail.get())
                b_insert_log('Success', 'Insert User', f'{user_name.get()} {user_family.get()} is added', '-')
                tkinter.messagebox.showinfo('Successful Message',
                                            f'New User: {user_name.get()} {user_family.get()} is added to database')
            else:
                tkinter.messagebox.showerror('Required Data', 'All Fields except Email is Required')
        except ConnectionError:
            b_insert_log('Failure', 'Insert User', 'New User is not added',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except ValueError:
            b_insert_log('Failure', 'Insert User', 'New User is not added',
                         'ValueError')
            tkinter.messagebox.showerror('ValueError', 'Something is wrong, try again later')
        except TclError:
            b_insert_log('Failure', 'Insert User', 'Type of data',
                         'TclError')
            tkinter.messagebox.showerror('TclError', 'Type of Age and Phone is Integer')


def add_book_window():
    add_home = Toplevel(home)
    v1 = add_home
    v1.title('Add Book')
    v1.geometry('300x300')
    v1.resizable(width=False, height=False)
    title = StringVar(value='')
    author = StringVar()
    cat_id = StringVar()
    book_year = IntVar(value='')
    isbn = StringVar()
    book_count = IntVar(value='')
    cat_list = dict(b_view_list_cat())
    value_list = cat_List_id()
    # ------------------------ add form --------------------
    text6 = Label(v1, text='Add New Book')
    text6.grid(row=0, column=0, columnspan=2, pady=10)
    text6.configure(font=font2)

    titleLabel = Label(v1, text='Title:* ')
    titleLabel.grid(row=1, column=0, pady=5, padx=5)
    titleEntry = Entry(v1, textvariable=title, width=30)
    titleEntry.grid(row=1, column=1, pady=5, padx=5)

    authorLabel = Label(v1, text='Author:* ')
    authorLabel.grid(row=2, column=0, pady=5, padx=5)
    authorEntry = Entry(v1, textvariable=author, width=30)
    authorEntry.grid(row=2, column=1, pady=5, padx=5)

    catLabel = Label(v1, text='Category:* ')
    catLabel.grid(row=3, column=0, pady=5, padx=5)
    cat_option = ttk.Combobox(v1, state='readonly', textvariable=cat_id, values=value_list, width=25)
    cat_option.grid(row=3, column=1, pady=5, padx=5)

    book_yearLabel = Label(v1, text='Book Year:* ')
    book_yearLabel.grid(row=4, column=0, pady=5, padx=5)
    book_yearEntry = Entry(v1, textvariable=book_year, width=30)
    book_yearEntry.grid(row=4, column=1, pady=5, padx=5)

    isbnLabel = Label(v1, text='ISBN:* ')
    isbnLabel.grid(row=5, column=0, pady=5, padx=5)
    isbnEntry = Entry(v1, textvariable=isbn, width=30)
    isbnEntry.grid(row=5, column=1, pady=5, padx=5)

    book_countLabel = Label(v1, text='Book Count:* ')
    book_countLabel.grid(row=6, column=0, pady=5, padx=5)
    book_countEntry = Entry(v1, textvariable=book_count, width=30)
    book_countEntry.grid(row=6, column=1, pady=5, padx=5)

    submit = Button(v1, text='Insert Book', width=20,
                    command=lambda: add_book(), bg='#217C7E', fg='White')
    submit.grid(row=7, column=0, columnspan=2)

    # ------------------------ add form --------------------
    def add_book():
        try:
            if title.get() and author.get() and cat_id.get() and book_year.get() and isbn.get() and book_count.get():
                b_add_book(title.get(), author.get(), book_year.get(), isbn.get(),
                           book_count.get(), cat_list[cat_id.get()])
                print((title.get(), author.get(), book_year.get(), isbn.get(),
                       book_count.get(), cat_id.get()))
                b_insert_log('Success', 'Insert Book', f'New Book: {title.get()} by {author.get()} is added', '-')
                tkinter.messagebox.showinfo('Successful Message', f'{title.get()} is added to database')
            else:
                tkinter.messagebox.showerror('Required Data', 'All Fields Are Required')
        except ConnectionError:
            b_insert_log('Failure', 'Insert Book', 'New Book is not added', 'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except ValueError:
            b_insert_log('Failure', 'Insert Book', 'New Book is not added', 'ValueError')
            tkinter.messagebox.showerror('ValueError', 'Something is wrong, try again later')
        except TclError:
            b_insert_log('Failure', 'Insert Book', 'Type of data', 'TclError')
            tkinter.messagebox.showerror('TclError', 'Type of Book Year and Book Count is Integer')


def add_category_window():
    cat_home = Toplevel(home)
    cat_home.title('Add Category')
    cat_home.geometry('380x260')
    cat_home.resizable(width=False, height=False)
    title = StringVar()
    tree_cat = ttk.Treeview(cat_home, column=("c1", "c2", "c3", "c4"), show='headings', height=5)
    tree_cat.column("#1", anchor=CENTER, width=7)
    tree_cat.heading("# 1", text="ID")
    tree_cat.column("# 2", anchor=CENTER, width=100)
    tree_cat.heading("# 2", text="Name")
    tree_cat.column("# 3", anchor=CENTER, width=130)
    tree_cat.heading("# 3", text="Created At")
    tree_cat.column("# 4", anchor=CENTER, width=130)
    tree_cat.heading("# 4", text="Updated At")
    tree_cat.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    # ------------------------ add form --------------------
    text6 = Label(cat_home, text='Add New Category')
    text6.grid(row=0, column=0, columnspan=2)
    text6.configure(font=font2)

    titleLabel = Label(cat_home, text='Name:* ')
    titleLabel.grid(row=1, column=0, pady=5, padx=5)
    titleEntry = Entry(cat_home, textvariable=title, width=30)
    titleEntry.grid(row=1, column=1, pady=5, padx=5)

    submit = Button(cat_home, text='Insert Category', width=20,
                    command=lambda: add_cat(), bg='#217C7E', fg='White')
    submit.grid(row=6, column=0, columnspan=2)

    # ------------------------ add form --------------------
    def add_cat():
        try:
            if title.get():
                b_add_category(title.get())
                b_insert_log('Success', 'Insert Category', f'New Category: {title.get()} is added', '-')
                tkinter.messagebox.showinfo('Successful Message', f'{title.get()} is added to database')
                view_all_cat()
            else:
                tkinter.messagebox.showerror('Required Data', 'All Fields Are Required')
        except ConnectionError:
            b_insert_log('Failure', 'Insert Category', 'New Category is not added', 'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except ValueError:
            b_insert_log('Failure', 'Insert Category', 'New Category is not added', 'ValueError')
            tkinter.messagebox.showerror('ValueError', 'Something is wrong, try again later')
        except:
            b_insert_log('Failure', 'Insert Category', 'Check', 'Unknown Error')
            tkinter.messagebox.showerror('Unknown Error', 'Something is Wrong, Try again later')

    def view_all_cat():
        try:
            for i in tree_cat.get_children():
                tree_cat.delete(i)
            cats = b_view_all_cat()
            for item in cats:
                tree_cat.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'View All Cat', 'Could not retrieve all Data from Category table',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    view_all_cat()


def update_book_window():
    update_Home = Toplevel(home)
    v1 = update_Home
    v1.title('Update Book')
    v1.geometry('920x350')
    # v1.resizable(width=False, height=False)
    tree_book = ttk.Treeview(v1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7"),
                             show='headings', height=13)
    tree_book.column("#1", anchor=CENTER, width=7)
    tree_book.heading("# 1", text="ID")
    tree_book.column("# 2", anchor=CENTER, width=170)
    tree_book.heading("# 2", text="Title")
    tree_book.column("# 3", anchor=CENTER, width=160)
    tree_book.heading("# 3", text="Author")
    tree_book.column("# 4", anchor=CENTER, width=100)
    tree_book.heading("# 4", text="Category")
    tree_book.column("# 5", anchor=CENTER, width=50)
    tree_book.heading("# 5", text="Year")
    tree_book.column("# 6", anchor=CENTER, width=80)
    tree_book.heading("# 6", text="ISBN")
    tree_book.column("# 7", anchor=CENTER, width=55)
    tree_book.heading("# 7", text="Count")
    tree_book.grid(row=0, column=3, padx=5, pady=10, rowspan=8)

    title = StringVar()
    author = StringVar()
    cat_id = StringVar()
    book_year = IntVar(value='')
    isbn = StringVar()
    book_count = IntVar(value='')
    book_id = IntVar(value='')
    cat_list = dict(b_view_list_cat())
    value_list = cat_List_id()

    def add_to_list():
        try:
            index = tree_book.focus()
            book_id.set(tree_book.item(index)["values"][0])
            title.set(tree_book.item(index)["values"][1])
            author.set(tree_book.item(index)["values"][2])
            cat_id.set(tree_book.item(index)["values"][3])
            book_year.set(tree_book.item(index)["values"][4])
            isbn.set(tree_book.item(index)["values"][5])
            book_count.set(tree_book.item(index)["values"][6])
        except IndexError:
            tkinter.messagebox.showerror('Error', 'No item is Selected')

    def update_book():
        try:
            if title.get() and author.get() and cat_id.get() and book_year.get() and isbn.get() and book_count.get():
                b_update_book(book_id.get(), title.get(), author.get(), cat_list[cat_id.get()], book_year.get(),
                              isbn.get(),
                              book_count.get())
                b_insert_log('Success', 'Update Book', f'Book: {title.get()} is updated', '-')
                tkinter.messagebox.showinfo('Successful Message', f'Book of {title.get()} is updated')
                view_all_update()
            else:
                tkinter.messagebox.showerror('Required Data', 'All Fields Are Required')
        except ConnectionError:
            b_insert_log('Failure', 'Update Book', 'Could not update the book', 'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except ValueError:
            b_insert_log('Failure', 'Update Book', 'Could not update the book', 'ValueError')
            tkinter.messagebox.showerror('ValueError', 'Something is wrong, try again later')
        except TclError:
            b_insert_log('Failure', 'Update Book', 'Type of data or required data', 'TclError')
            tkinter.messagebox.showerror('TclError', 'Type of Book Year and Book Count is Integer')

    def view_all_update():
        try:
            for i in tree_book.get_children():
                tree_book.delete(i)
            books = b_view_all_book()
            for item in books:
                tree_book.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'View All Tree', 'Could not retrieve all Data from user or book table',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    # ------------------------ add form --------------------
    text7 = Label(v1, text='Update a Book')
    text7.grid(row=0, column=0, columnspan=2, pady=5)
    text7.configure(font=font2)

    book_id_label = Label(v1, text='Book ID: *')
    book_id_label.grid(row=1, column=0, pady=5, padx=5)
    book_id_input = Label(v1, textvariable=book_id, width=25)
    book_id_input.grid(row=1, column=1, pady=10, padx=5)

    titleLabel = Label(v1, text='Title: ')
    titleLabel.grid(row=2, column=0, pady=5, padx=5)
    titleEntry = Entry(update_Home, textvariable=title, width=25)
    titleEntry.grid(row=2, column=1, pady=5, padx=5)

    authorLabel = Label(v1, text='Author: ')
    authorLabel.grid(row=3, column=0, pady=5, padx=5)
    authorEntry = Entry(v1, textvariable=author, width=25)
    authorEntry.grid(row=3, column=1, pady=5, padx=5)

    catLabel = Label(v1, text='Category:* ')
    catLabel.grid(row=4, column=0, pady=5, padx=5)
    cat_option = ttk.Combobox(v1, state='readonly', textvariable=cat_id, values=value_list, width=20)
    cat_option.grid(row=4, column=1, pady=5, padx=5)

    book_yearLabel = Label(v1, text='Book Year: ')
    book_yearLabel.grid(row=5, column=0, pady=5, padx=5)
    book_yearEntry = Entry(v1, textvariable=book_year, width=25)
    book_yearEntry.grid(row=5, column=1, pady=5, padx=5)

    isbnLabel = Label(v1, text='isbn: ')
    isbnLabel.grid(row=6, column=0, pady=5, padx=5)
    isbnEntry = Entry(v1, textvariable=isbn, width=25)
    isbnEntry.grid(row=6, column=1, pady=5, padx=5)

    book_countLabel = Label(v1, text='Book Count: ')
    book_countLabel.grid(row=7, column=0, pady=5, padx=5)
    book_countEntry = Entry(v1, textvariable=book_count, width=25)
    book_countEntry.grid(row=7, column=1, pady=5, padx=5)

    update_button = Button(v1, text='Update Book', width=25, command=update_book, bg='#217C7E', fg='White')
    update_button.grid(row=8, column=0, columnspan=2)
    add_button = Button(v1, text='Add to List', width=25, command=add_to_list, bg='#217C7E', fg='White')
    add_button.grid(row=8, column=2, columnspan=2)

    view_all_update()


def logs_window():
    log_home = Toplevel(home)
    v1 = log_home
    v1.title('Logs History')
    v1.geometry('770x400')
    # v1.resizable(width=False, height=False)
    log_status = StringVar()
    log_type = StringVar()
    log_desc = StringVar()
    log_fail_status = StringVar()
    created_at = StringVar()
    fail_desc_list = ['ConnectionError', 'TclError', 'ValueError', 'UnknownError', 'KeyError']

    tree_search = ttk.Treeview(v1, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height=10)
    tree_search.column("#1", anchor=CENTER, width=7)
    tree_search.heading("# 1", text="ID")
    tree_search.column("# 2", anchor=CENTER, width=80)
    tree_search.heading("# 2", text="Status")
    tree_search.column("# 3", anchor=CENTER, width=120)
    tree_search.heading("# 3", text="Log Type")
    tree_search.column("# 4", anchor=CENTER, width=270)
    tree_search.heading("# 4", text="Description")
    tree_search.column("# 5", anchor=CENTER, width=110)
    tree_search.heading("# 5", text="Fail Desc")
    tree_search.column("# 6", anchor=CENTER, width=130)
    tree_search.heading("# 6", text="Created At")
    tree_search.grid(row=3, column=0, padx=5, pady=5, columnspan=6)

    def clear_logs_history():
        msg = tkinter.messagebox.askquestion('Drop All Logs', 'Do you want to drop Logs table?!')
        if msg == 'yes':
            try:
                b_logs_drop()
                tkinter.messagebox.showinfo('Successful', 'The table of Logs deleted completely')
                view_all_logs()
            except ConnectionError:
                b_insert_log('Failure', 'Drop Log Table', 'Could not drop table', 'ConnectionError')
                tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    def clear_logs():
        log_status.set('')
        log_type.set('')
        log_desc.set('')
        log_fail_status.set('')
        created_at.set('')

    def view_a_log():
        try:
            index = tree_search.focus()
            tkinter.messagebox.showinfo('Log Information', f'Log ID:    {tree_search.item(index)["values"][0]}\n'
                                                           f'Status:    {tree_search.item(index)["values"][1]}\n'
                                                           f'Log Type:   {tree_search.item(index)["values"][2]}\n'
                                                           f'Description:   {tree_search.item(index)["values"][3]}\n'
                                                           f'Fail Desc:    {tree_search.item(index)["values"][4]}\n'
                                                           f'Created At:    {tree_search.item(index)["values"][5]}')
        except IndexError:
            tkinter.messagebox.showerror('Error', 'No item is Selected')

    def search_log():
        try:
            for i in tree_search.get_children():
                tree_search.delete(i)
            result_logs = b_search_logs(log_status.get(), log_type.get(), log_desc.get(),
                                        log_fail_status.get(), created_at.get())
            if len(result_logs) == 0:
                tkinter.messagebox.showinfo('No Result', 'No item is matched')
                view_all_logs()
                clear_logs()
            else:
                for item in result_logs:
                    tree_search.insert('', 'end', values=item)
            for item in result_logs:
                tree_search.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'Search Log', 'Could not retrieve data', 'ConnectionError')
            tkinter.messagebox.showerror('Error', 'Database is not available')

    def delete_log():
        try:
            index = tree_search.focus()
            selected = tree_search.item(index)["values"][0]
            msg = tkinter.messagebox.askquestion('Delete', f'Do you want to delete log_id: {selected} ?')
            if msg == 'yes':
                try:
                    tkinter.messagebox.showinfo('Successful Operation', f'{selected} is deleted!')
                    b_del_log(selected)
                    b_insert_log('Success', 'Delete Log', f'{selected} is deleted', '-')
                    view_all_logs()
                except ConnectionError:
                    b_insert_log('Failure', 'Delete Log', f'Could not delete {selected}',
                                 'ConnectionError')
                    tkinter.messagebox.showerror('Error', 'Database is not available')
        except IndexError:
            tkinter.messagebox.showerror('Selected Error', 'No Item is Selected!!!')

    def view_all_logs():
        try:
            for i in tree_search.get_children():
                tree_search.delete(i)
            books = b_view_all_logs()
            for item in books:
                tree_search.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'View All Logs', 'Could not retrieve all Data', 'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    text1 = Label(v1, text='Search it')
    text1.grid(row=1, column=0, padx=5)
    text1.configure(font=font1)

    preview = Button(v1, text='Preview', width=7, command=view_a_log)
    preview.grid(row=2, column=0)

    status_label = Label(v1, text='Status')
    status_label.grid(row=0, column=1, pady=5, padx=5)
    status_combo = ttk.Combobox(v1, textvariable=log_status, width=17, values=('Success', 'Failure'), state='readonly')
    status_combo.grid(row=1, column=1, pady=5, padx=5)

    logtypelabel = Label(v1, text='Log Type')
    logtypelabel.grid(row=0, column=2, pady=5, padx=5)
    logtypeentry = Entry(v1, textvariable=log_type, width=15)
    logtypeentry.grid(row=1, column=2, pady=5, padx=5)

    desc_label = Label(v1, text='Description')
    desc_label.grid(row=0, column=3, pady=5, padx=5)
    desc_entry = Entry(v1, textvariable=log_desc, width=20)
    desc_entry.grid(row=1, column=3, pady=5, padx=5)

    fd_label = Label(v1, text='Fail Description')
    fd_label.grid(row=0, column=4, pady=5, padx=5)
    fd_combo = ttk.Combobox(v1, textvariable=log_fail_status, width=20, values=fail_desc_list, state='readonly')
    # fd_entry = Entry(v1, textvariable=log_fail_status, width=20)
    fd_combo.grid(row=1, column=4, pady=5, padx=5)

    ld_label = Label(v1, text='Log Date')
    ld_label.grid(row=0, column=5, pady=5, padx=5)
    ld_entry = Entry(v1, textvariable=created_at, width=20)
    ld_entry.grid(row=1, column=5, pady=5, padx=5)

    list_logs = Listbox(v1, width=80)
    # list_logs.grid(row=1, column=2, rowspan=6)

    search_button_or = Button(v1, text='Search And', command=search_log, width=10, bg='#217C7E', fg='White')
    search_button_or.grid(row=2, column=1, pady=5)

    del_log = Button(v1, text='Delete a log', width=10, command=delete_log)
    del_log.grid(row=2, column=2, pady=5)

    view_all = Button(v1, text='View All', command=view_all_logs, width=9)
    view_all.grid(row=2, column=3, pady=5)

    drop_history = Button(v1, text='Clear All History', command=clear_logs_history, width=15)
    drop_history.grid(row=2, column=4, pady=5)

    clear = Button(v1, text='Clear Form', width=11, command=clear_logs)
    clear.grid(row=2, column=5, pady=5)

    view_all_logs()


def search_book_window():
    search_home = Toplevel(home)
    v1 = search_home
    v1.title('Search Book')
    v1.geometry('900x360')
    v1.resizable(width=False, height=False)
    title = StringVar()
    author = StringVar()
    cat_id = StringVar()
    book_year = StringVar()
    isbn = StringVar()
    book_count = StringVar()
    cat_list = dict(b_view_list_cat())
    value_list = cat_List_id()

    tree_search = ttk.Treeview(v1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"),
                               show='headings',
                               height=10)
    tree_search.column("#1", anchor=CENTER, width=7)
    tree_search.heading("# 1", text="ID")
    tree_search.column("# 2", anchor=CENTER, width=170)
    tree_search.heading("# 2", text="Title")
    tree_search.column("# 3", anchor=CENTER, width=160)
    tree_search.heading("# 3", text="Author")
    tree_search.column("# 4", anchor=CENTER, width=100)
    tree_search.heading("# 4", text="Category")
    tree_search.column("# 5", anchor=CENTER, width=50)
    tree_search.heading("# 5", text="Year")
    tree_search.column("# 6", anchor=CENTER, width=80)
    tree_search.heading("# 6", text="ISBN")
    tree_search.column("# 7", anchor=CENTER, width=55)
    tree_search.heading("# 7", text="Count")
    tree_search.column("# 8", anchor=CENTER, width=130)
    tree_search.heading("# 8", text="Created At")
    tree_search.column("# 9", anchor=CENTER, width=130)
    tree_search.heading("# 9", text="Updated At")
    tree_search.grid(row=3, column=0, padx=5, pady=5, columnspan=6)

    def clear():
        title.set('')
        author.set('')
        cat_id.set('')
        book_year.set('')
        isbn.set('')
        book_count.set('')

    def view_a_book():
        try:
            index = tree_search.focus()
            tkinter.messagebox.showinfo('Book Information', f'Book ID:    {tree_search.item(index)["values"][0]}\n'
                                                            f'Title:    {tree_search.item(index)["values"][1]}\n'
                                                            f'Author:   {tree_search.item(index)["values"][2]}\n'
                                                            f'Category:   {tree_search.item(index)["values"][3]}\n'
                                                            f'Book Year:    {tree_search.item(index)["values"][4]}\n'
                                                            f'ISBN:    {tree_search.item(index)["values"][5]}\n'
                                                            f'Book Count:   {tree_search.item(index)["values"][6]}\n'
                                                            f'Created At:   {tree_search.item(index)["values"][7]}\n'
                                                            f'Updated At:   {tree_search.item(index)["values"][8]}')
        except IndexError:
            tkinter.messagebox.showerror('Error', 'No item is Selected')

    def search_book_and():
        if title.get() == '':
            title_v = None
        else:
            title_v = title.get()

        if author.get() == '':
            author_v = None
        else:
            author_v = author.get()

        if book_year.get() == '':
            book_year_v = None
        else:
            book_year_v = book_year.get()

        if cat_id.get() == '':
            cat_id_v = None
        else:
            cat_id_v = cat_list[cat_id.get()]

        if isbn.get() == '':
            isbn_v = None
        else:
            isbn_v = isbn.get()

        if book_count.get() == '':
            book_count_v = None
        else:
            book_count_v = book_count.get()

        try:
            for i in tree_search.get_children():
                tree_search.delete(i)
            result_books = b_search_book_and(title_v, author_v, cat_id_v, book_year_v,
                                             isbn_v, book_count_v)
            if len(result_books) == 0:
                tkinter.messagebox.showinfo('No Result', 'No item is matched\n'
                                                         'Be careful About CapsLock on/off')
                view_all_search()
            else:
                for item in result_books:
                    tree_search.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'ASearch Book', 'Could not retrieve data',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

        except TclError:
            b_insert_log('Failure', 'ASearch Book', 'Could not retrieve data', 'TclError')
            tkinter.messagebox.showerror('TclError', 'Something is Wrong')
            view_all_search()

    def search_book_or():
        try:
            for i in tree_search.get_children():
                tree_search.delete(i)
            result_books = b_search_book_or(title.get(), author.get(), cat_list[cat_id.get()], book_year.get(),
                                            isbn.get(), book_count.get())
            if len(result_books) == 0:
                tkinter.messagebox.showinfo('No Result', 'No item is matched\n'
                                                         'Be careful About CapsLock\n')
                view_all_search()
            else:
                for item in result_books:
                    tree_search.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'OSearch Book', 'Could not retrieve data', 'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except TclError:
            b_insert_log('Failure', 'OSearch Book', 'Could not retrieve data', 'TclError')
            tkinter.messagebox.showerror('TclError', 'Type of Book Year and Book Count is Integer')
            view_all_search()
        except KeyError:
            b_insert_log('Failure', 'OSearch Book', 'No category is selected', 'KeyError')
            tkinter.messagebox.showinfo('No Result', 'No category is selected')

    def view_all_search():
        try:
            for i in tree_search.get_children():
                tree_search.delete(i)
            books = b_view_all_book()
            for item in books:
                tree_search.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'View All Tree', 'Could not retrieve all Data from user or book table',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    # ------------------------ add form --------------------
    titleLabel = Label(v1, text='Title')
    titleLabel.grid(row=0, column=0, pady=5, padx=5)
    titleEntry = Entry(v1, textvariable=title, width=30)
    titleEntry.grid(row=1, column=0, pady=5, padx=5)

    authorLabel = Label(v1, text='Author')
    authorLabel.grid(row=0, column=1, pady=5, padx=5)
    authorEntry = Entry(v1, textvariable=author, width=25)
    authorEntry.grid(row=1, column=1, pady=5, padx=5)

    catLabel = Label(v1, text='Category')
    catLabel.grid(row=0, column=2, pady=5, padx=5)
    cat_option = ttk.Combobox(v1, state='readonly', textvariable=cat_id, values=value_list, width=20)
    cat_option.grid(row=1, column=2, pady=5, padx=5)

    book_yearLabel = Label(v1, text='Book Year')
    book_yearLabel.grid(row=0, column=3, pady=5, padx=5)
    book_yearEntry = Entry(v1, textvariable=book_year, width=15)
    book_yearEntry.grid(row=1, column=3, pady=5, padx=5)

    isbnLabel = Label(v1, text='ISBN')
    isbnLabel.grid(row=0, column=4, pady=5, padx=5)
    isbnEntry = Entry(v1, textvariable=isbn, width=20)
    isbnEntry.grid(row=1, column=4, pady=5, padx=5)

    book_countLabel = Label(v1, text='Book Count')
    book_countLabel.grid(row=0, column=5, pady=5, padx=5)
    book_countEntry = Entry(v1, textvariable=book_count, width=15)
    book_countEntry.grid(row=1, column=5, pady=5, padx=5)

    text1 = Label(v1, text='Choose Button')
    text1.grid(row=2, column=0)
    text1.configure(font=font1)
    view_all = Button(v1, text='View All', command=view_all_search, width=7)
    view_all.grid(row=2, column=1, pady=5)

    view = Button(v1, text='Preview', width=7, command=view_a_book)
    view.grid(row=2, column=2)

    search_button_or = Button(v1, text='Search OR', command=search_book_or, bg='#217C7E', fg='White')
    search_button_or.grid(row=2, column=3, pady=5)

    search_button_and = Button(v1, text='Search AND', command=search_book_and, bg='#217C7E', fg='White')
    search_button_and.grid(row=2, column=4, pady=5)

    clear = Button(v1, text='Clear Form', width=10, command=clear)
    clear.grid(row=2, column=5, pady=5)

    view_all_search()


def delete_book_window():
    delete_home = Toplevel(home)
    v1 = delete_home
    v1.title('Delete a Book')
    v1.geometry('900x300')
    v1.resizable(width=False, height=False)
    tree_book = ttk.Treeview(v1, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9"),
                             show='headings',
                             height=10)
    tree_book.column("#1", anchor=CENTER, width=7)
    tree_book.heading("# 1", text="ID")
    tree_book.column("# 2", anchor=CENTER, width=170)
    tree_book.heading("# 2", text="Title")
    tree_book.column("# 3", anchor=CENTER, width=160)
    tree_book.heading("# 3", text="Author")
    tree_book.column("# 4", anchor=CENTER, width=100)
    tree_book.heading("# 4", text="Category")
    tree_book.column("# 5", anchor=CENTER, width=50)
    tree_book.heading("# 5", text="Year")
    tree_book.column("# 6", anchor=CENTER, width=80)
    tree_book.heading("# 6", text="ISBN")
    tree_book.column("# 7", anchor=CENTER, width=55)
    tree_book.heading("# 7", text="Count")
    tree_book.column("# 8", anchor=CENTER, width=130)
    tree_book.heading("# 8", text="Created At")
    tree_book.column("# 9", anchor=CENTER, width=130)
    tree_book.heading("# 9", text="Updated At")
    tree_book.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def view_all_delete():
        try:
            for i in tree_book.get_children():
                tree_book.delete(i)
            books = b_view_all_book()
            for item in books:
                tree_book.insert('', 'end', values=item)
        except ConnectionError:
            b_insert_log('Failure', 'View All Tree', 'Could not retrieve all Data from user or book table',
                         'ConnectionError')
            tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    def delete_book():
        try:
            index = tree_book.focus()
            selected = tree_book.item(index)["values"][1]
            msg = tkinter.messagebox.askquestion('Delete',
                                                 f'Do you want to delete {tree_book.item(index)["values"][1]} ?')
            if msg == 'yes':
                try:
                    tkinter.messagebox.showinfo('Successful Operation', f'{selected} is deleted!')
                    b_del_book(tree_book.item(index)["values"][0])
                    b_insert_log('Success', 'Delete Book', f'{selected} is deleted', '-')
                    view_all_delete()
                except ConnectionError:
                    b_insert_log('Failure', 'Delete Book', f'Could not delete {selected}',
                                 'ConnectionError')
                    tkinter.messagebox.showerror('ConnectionError', 'Database is not available')
        except IndexError:
            tkinter.messagebox.showerror('Selected Error', 'No Item is Selected!!!')

    # ------------------------ add form --------------------
    text8 = Label(v1, text='If you Want to delete a book, Select it then click on Delete')
    text8.grid(row=0, column=0)
    text8.configure(font=font2)

    delete_button = Button(v1, text='Delete It', command=delete_book, width=20, bg='#9A3334', fg='White')
    delete_button.grid(row=0, column=1, pady=5)

    view_all_delete()


def db_tools_window():
    db_tools_home = Toplevel(home)
    v1 = db_tools_home
    v1.title('DB Tools')
    v1.geometry('300x240')
    v1.resizable(width=False, height=False)

    def delete_db():
        msg = tkinter.messagebox.askquestion('Caution !!!', f'If you continue!,\n'
                                                            f'All DB data will be Vanished\n\n'
                                                            f'Are you Sure to continue???')
        if msg == 'yes':
            try:
                b_delete_db()
                tkinter.messagebox.showinfo('Successful Operation', 'Your Database is Deleted')
                b_insert_log('Success', 'Delete DB', 'Your Database is deleted', '-')

            except ConnectionError:
                b_insert_log('Failure', 'Delete DB', f'Could not Delete DB',
                             'ConnectionError')
                tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    def import_db():
        msg = tkinter.messagebox.askquestion('Caution !!!', f'Do you want to import sample data?')
        if msg == 'yes':
            try:
                b_import_data()
                tkinter.messagebox.showinfo('Successful Operation', 'Your Database is Upgraded')
                b_insert_log('Success', 'Import DB', 'Your Database is Upgraded', '-')

            except ConnectionError:
                b_insert_log('Failure', 'Import DB', f'Could not import new Data',
                             'ConnectionError')
                tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

    del_label = Label(v1, text='Are you Sure you want to Delete Whole your db,\n\n '
                               'click the below button')
    del_label.grid(row=0, column=0, pady=7)
    del_label.configure(font=font2)
    del_button = Button(v1, text='Delete Database', command=delete_db, bg='#9A3334', fg='White')
    del_button.grid(row=1, column=0, pady=7)

    import_label = Label(v1, text='Do you want to import data in your db,\n\n '
                                  'click the below button')
    import_label.grid(row=2, column=0, pady=7)
    import_label.configure(font=font2)
    import_button = Button(v1, text='Import Database', command=import_db, bg='#9A3334', fg='White')
    import_button.grid(row=3, column=0, pady=7)


# .......................... Final Functions .......................
try:
    b_connect()
    view_all_home()
except ConnectionError:
    tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

home.configure(menu=topMenu)
home.mainloop()
