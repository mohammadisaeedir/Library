import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.categories import b_view_list_cat
from src.repositories.fileConfig import cat_List_id
from src.repositories.logs import b_insert_log
from src.views.home import home, font1
from src.repositories.books import b_search_book_or, b_search_book_and, b_view_all_book


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
