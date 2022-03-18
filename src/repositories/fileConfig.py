import sqlite3
from src.repositories.categories import b_view_list_cat

db_name = 'libdb'


def b_connect():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'create table if not exists category (cat_id INTEGER PRIMARY KEY, cat_name VARCHAR NOT NULL, created_at DATE '
        'NOT NULL, '
        'updated_at DATE NOT NULL)')
    cur.execute(
        'create table if not exists book (book_id INTEGER PRIMARY KEY, title VARCHAR NOT NULL, author VARCHAR NOT '
        'NULL, book_year INTEGER NOT NULL, isbn varchar NOT NULL, book_count integer NOT '
        'NULL, created_at DATE NOT NULL, updated_at DATE NOT NULL, cat_id INTEGER NOT NULL, FOREIGN KEY(cat_id) '
        'REFERENCES '
        'category(cat_id))')
    cur.execute(
        'create table if not exists user (user_id INTEGER PRIMARY KEY, user_name VARCHAR NOT NULL, '
        'user_family VARCHAR NOT NULL, user_age INTEGER NOT NULL, user_phone INTEGER NOT NULL, mail varchar, '
        'created_at DATE NOT NULL, updated_at '
        'DATE NOT NULL)')
    cur.execute(
        'create table if not exists logs (log_id INTEGER PRIMARY KEY, status VARCHAR, log_type VARCHAR, '
        'description VARCHAR, fail_description VARCHAR, created_at DATE)')
    cur.execute(
        'create table if not exists reserve (reserve_id INTEGER PRIMARY KEY, user_id VARCHAR NOT NULL, '
        'book_id VARCHAR NOT NULL, count INTEGER NOT NULL, status VARCHAR NOT NULL, duration INTEGER NOT '
        'NULL, created_at DATE NOT NULL)')
    connection.commit()
    connection.close()


def b_delete_db():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from user')
    cur.execute('delete from book')
    cur.execute('delete from category')
    cur.execute('delete from logs')
    cur.execute('delete from reserve')
    connection.commit()
    connection.close()


def b_import_data():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sqluser = [
        ('Hossein', 'Rezaeizadeh', 22, '9391234321', 'h.rezaeizadeh@gmail.com', '2022-02-12 22:12:40',
         '2022-04-15 10:14:26'),
        ('Saeed', 'Ghasemi', 27, '9309876543', 'saeedghasemi1372@gmail.com', '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Karim', 'Benzema', 34, '9122105271', 'karimbenzema@gmail.com', '2020-05-05 10:20:46',
         '2020-05-05 10:04:26'),
        ('Saeed', 'Mohammadi', 34, '9356706868', 'mohammadisaeedir@gmail.com', '2022-03-12 13:00:46',
         '2022-03-11 13:04:26'),
        ('Zeinab', 'Rezaeizadeh', 33, '9364637883', 'z3inab.rezaei@gmail.com', '2022-05-22 13:01:46',
         '2022-04-21 00:24:26')
    ]
    stmt = "insert into user (user_name, user_family, user_age, user_phone, mail, created_at, updated_at) " \
           "values (?, ?, ?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqluser)
    sqlbook = [
        ('Strategy', 'Engolo Cante', 4, 1987, 'L23451', 2500, '2022-02-12 22:12:40',
         '2022-04-15 10:14:26'),
        ('Knowledge', 'Fede Valverde', 2, 1990, 'S23452', 3000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Python', 'Simon Kayer', 1, 1991, 'M21343', 1000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Django', 'Saeed Rezaei', 3, 2010, 'K12345', 8000, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10'),
        ('Real Madrid', 'Sergio Ramoos', 1, 1989, 'V23452', 3500, '2021-09-01 17:50:46',
         '2021-12-11 20:10:10')
    ]
    stmt = "insert into book (title, author, cat_id, book_year, isbn, book_count, created_at, updated_at) " \
           "values (?, ?, ?, ?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqlbook)
    sqlcategory = [
        ('History', '2022-05-02 22:12:40', '2022-14-15 11:34:26'),
        ('Science', '2020-12-11 22:12:40', '2022-08-15 10:24:26'),
        ('Sport', '2021-02-03 22:12:40', '2022-04-15 20:17:26'),
        ('Programing', '2022-02-12 22:12:40', '2022-14-15 12:14:26')
    ]
    stmt = "insert into category (cat_name, created_at, updated_at) values (?, ?, ?)"
    cur.executemany(stmt, sqlcategory)
    sqllogs = [
        ('Success', 'Insert User', 'Saeed Mohammadi is added', '-', '2022-22-12 10:55:26'),
        ('Failure', 'Delete User', 'User id: 1 is deleted', 'ConnectionError', '2022-14-10 11:24:16'),
        ('Success', 'Insert User', 'Zeinab Rezaeizadeh is added', '-', '2022-13-08 17:11:36'),
        ('Failure', 'Delete Book', 'Book Id: 6 is deleted', 'TclError', '2022-21-07 11:22:44'),
        ('Success', 'Delete Book', 'Book Id: 8 is deleted', '-', '2022-21-07 11:22:44'),
        ('Success', 'Insert Book', 'Strategy by Engolo Cante is added', '-', '2022-06-01 21:54:46'),
        ('Success', 'Insert Book', 'Knowledge by Fede Valverde is added', '-', '2022-06-01 21:54:46'),
        ('Success', 'Insert Category', 'The Category: Sport is added', '-', '2021-06-01 21:54:46'),
        ('Success', 'Update Book', 'Python by Simon Kayer is Updated', '-', '2021-12-04 00:10:41'),
        ('Failure', 'Update User', 'Saeed Mohammadi is Updated', 'TclError', '2021-11-04 04:50:49'),
        ('Success', 'Insert Book', 'Flask by Python Developer is added', '-', '2021-10-02 15:40:43'),
        ('Success', 'Insert Book', 'Python by Simon Kayer is added', '-', '2021-10-02 15:40:43')
    ]
    stmt = "insert into logs (status, log_type, description, fail_description, created_at) " \
           "values (?, ?, ?, ?, ?)"
    cur.executemany(stmt, sqllogs)
    connection.commit()
    connection.close()


def cat_List_id():
    cat_list = dict(b_view_list_cat())
    value_list = []
    for value in cat_list.keys():
        value_list.append(value)
    return value_list
