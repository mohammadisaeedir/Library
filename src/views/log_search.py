import tkinter.messagebox
from tkinter import *
from tkinter import ttk

from src.repositories.logs import b_logs_drop, b_del_log, b_insert_log, b_view_all_logs, b_search_logs
from src.views.home import home

font1 = ("Comic Sans MS", 13, "bold")


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
        msg = tkinter.messagebox.askquestion('Drop All Logs', 'Do you want to \"drop\" Logs table?!')
        if msg == 'yes':
            try:
                b_logs_drop()
                tkinter.messagebox.showinfo('Successful', 'The Table of Logs Deleted Completely')
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
