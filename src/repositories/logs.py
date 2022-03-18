import datetime
import sqlite3

db_name = 'libdb'


def b_insert_log(status, log_type, desc, fail_desc):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('insert into logs values (NULL, ?,?,?,?,?)',
                (status, log_type, desc, fail_desc, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    connection.commit()
    connection.close()


def b_count_del():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Delete Book' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_books():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert Book' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_users():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert User' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_count_category():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    sql = """
        select count(log_id) from logs where log_type like 'Insert Category' and status = 'Success'
    """
    cur.execute(sql)
    result = cur.fetchone()[0]
    connection.commit()
    connection.close()
    return result


def b_search_logs(log_status='', log_type='', log_desc='', log_faildesc='', created_at=''):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute(
        'select * from logs where status like ? and log_type like ? and '
        'description like ? and  fail_description like ? and created_at like ?',
        ('%' + log_status + '%', '%' + log_type + '%', '%' + log_desc + '%',
         '%' + log_faildesc + '%', '%' + created_at + '%'))
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_view_all_logs():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('select * from logs order by log_id desc ')
    rows = cur.fetchall()
    connection.commit()
    connection.close()
    return rows


def b_del_log(log_id):
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from logs where log_id=?', (log_id,))
    connection.commit()
    connection.close()


def b_logs_drop():
    connection = sqlite3.connect(db_name)
    cur = connection.cursor()
    cur.execute('delete from logs')
    connection.commit()
    connection.close()