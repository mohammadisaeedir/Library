import sqlite3
import datetime

db_name = 'libdb'


def b_add_category(name):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into category values (NULL, ?,?,?)',
                (name, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_view_all_cat():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select cat_id, cat_name, created_at, updated_at '
        'from category order by cat_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_view_list_cat():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select distinct cat_name, cat_id '
        'from category group by cat_name order by cat_name')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows