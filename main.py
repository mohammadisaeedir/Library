import tkinter.messagebox
from tkinter import *

from src.repositories.fileConfig import b_connect
from src.views.DB_tools import db_tools_window
from src.views.add_book import add_book_window
from src.views.add_category import add_category_window
from src.views.add_user import add_user_view
from src.views.book_search import search_book_window
from src.views.delete_book import delete_book_window
from src.views.home import home, nothing, report_home, font2, view_all_home, view_a_book, view_a_user, books_num, users_num, dels_num, cat_num
from src.views.log_search import logs_window
from src.views.update_book import update_book_window

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

try:
    b_connect()
    view_all_home()
except ConnectionError:
    tkinter.messagebox.showerror('ConnectionError', 'Database is not available')

home.configure(menu=topMenu)
home.mainloop()
