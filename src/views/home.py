import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.books import b_view_all_book

from src.repositories.logs import *
from src.repositories.users import b_view_all_user

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


