import tkinter.messagebox
from tkinter import *


from src.views.home import home, font2
from src.repositories.fileConfig import b_delete_db, b_import_data
from src.repositories.logs import b_insert_log

def db_tools_window():
    db_tools_home = Toplevel(home)
    v1 = db_tools_home
    v1.title('DB Tools')
    v1.geometry('300x240')
    v1.resizable(width=False, height=False)

    def delete_db():
        msg = tkinter.messagebox.askquestion('Caution !!!', f'If you continue!,\n'
                                                            f'All DB data will be \"Vanished\"\n\n'
                                                            f'Are you Sure to continue???')
        if msg == 'yes':
            try:
                b_delete_db()
                tkinter.messagebox.showinfo('Successful Operation', 'Your Database is Completely Deleted')
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
                tkinter.messagebox.showinfo('Successful Operation', 'Your Database is Upgraded by sample data')
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

    import_label = Label(v1, text='If you want to import data in your db,\n\n '
                                  'click the below button')
    import_label.grid(row=2, column=0, pady=7)
    import_label.configure(font=font2)
    import_button = Button(v1, text='Import Database', command=import_db, bg='#9A3334', fg='White')
    import_button.grid(row=3, column=0, pady=7)
