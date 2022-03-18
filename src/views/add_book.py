import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.books import b_add_book
from src.repositories.fileConfig import b_view_list_cat, cat_List_id
from src.repositories.logs import b_insert_log
from src.views.home import home, font2


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
