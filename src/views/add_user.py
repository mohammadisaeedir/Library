import tkinter.messagebox
from tkinter import *
from src.views.home import home
from src.repositories.logs import b_insert_log
from src.repositories.users import b_add_user



font2 = ("Comic Sans MS", 10)


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
