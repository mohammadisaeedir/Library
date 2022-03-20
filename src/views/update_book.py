import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.books import b_update_book, b_view_all_book
from src.repositories.categories import b_view_list_cat
from src.repositories.fileConfig import cat_List_id
from src.repositories.logs import b_insert_log
from src.views.home import home

font2 = ("Comic Sans MS", 10)


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
                tkinter.messagebox.showinfo('Successful Message', f'Book of \"{title.get()}\" is updated')
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
