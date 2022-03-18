import datetime
import sqlite3

db_name = 'libdb'


def b_add_book(title, author, book_year, isbn, book_count, cat_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into book values (NULL, ?,?,?,?,?,?,?,?)',
                (title, author, book_year, isbn, book_count,
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cat_id))
    connection.commit()
    connection.close()


def b_update_book(book_id, title, author, cat_id, book_year, isbn, book_count):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('update book set title=?, author=?, cat_id=?, book_year=?, isbn=?, '
                'book_count=?, updated_at=? where book_id=?',
                (title, author, cat_id, book_year, isbn, book_count,
                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 book_id))
    connection.commit()
    connection.close()


def b_search_book_or(title='', author='', cat_id='', book_year='', isbn='', book_count=''):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book where title like ? or author like ? or cat_id like ? or '
        'book_year like ? or isbn like ? or '
        'book_count like ?', (title, author, cat_id, book_year, isbn, book_count))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_search_book_and(title=None, author=None, cat_id=None, book_year=None, isbn=None, book_count=None):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book where title=coalesce(?,title) and '
        'author=coalesce(?,author) and cat_id=coalesce(?,cat_id) and book_year=coalesce(?,book_year) and '
        'isbn=coalesce(?,isbn) and book_count=coalesce(?,book_count)',
        (title, author, cat_id, book_year, isbn, book_count))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_del_book(book_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from book where book_id=?', (book_id,))
    connection.commit()
    connection.close()


def b_view_all_book():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select book_id, title, author, (select cat_name from category where book.cat_id=category.cat_id), book_year, '
        'isbn, book_count, created_at, updated_at from book order by book_id desc')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows