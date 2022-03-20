from tkinter import *
from tkinter import ttk
from src.views.home import home
import tkinter.messagebox
from src.repositories.logs import b_insert_log
from src.repositories.categories import b_add_category, b_view_all_cat

font2 = ("Comic Sans MS", 10)


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
                tkinter.messagebox.showinfo('Successful Message', f'\"{title.get()}\" is added to database')
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
