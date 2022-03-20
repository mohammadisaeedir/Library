import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.books import b_view_all_book, b_del_book
from src.repositories.logs import b_insert_log
from src.views.home import home, font2


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
                    tkinter.messagebox.showinfo('Successful Operation', f'\"{selected}\" is deleted!')
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
