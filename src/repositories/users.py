import datetime
import sqlite3

db_name = 'libdb'


def b_add_user(name, family, age, phone, mail):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into user values (NULL, ?,?,?,?,?,?,?)',
                (name, family, age, phone, mail, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_view_all_user():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('select * from user order by user_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows