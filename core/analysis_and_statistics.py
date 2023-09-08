import sqlite3
from datetime import datetime, timezone

from settings import DB_PATH
from core.log_conf import create_logger

'''
db - users_data
table - users
id | username | timestamp

'''

logger = create_logger(__name__, 'db.log')


def db_decorator(func):
    def db_wrapper(*args):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        params = (cur, con) + args
        return func(*params)

    return db_wrapper


@db_decorator
def add_user(*args):
    try:
        cur, con, _id, username = args

        logger.info(f'ADD NEW USER - {username}')
        now = datetime.now(timezone.utc)
        cur.execute(
            'INSERT INTO users VALUES (?, ?, ?);',
            (_id, username, now)
        )
        con.commit()
        return 0
    except Exception as e:
        logger.error(e)
    return 1


@db_decorator
def get_all_users(*args):
    cur = args[0]
    res = cur.execute('SELECT id, username FROM users ORDER BY time DESC;')
    return res.fetchall()


@db_decorator
def get_last_five_users(*args):
    cur = args[0]
    res = cur.execute(
        'SELECT id, username FROM users ORDER BY time DESC LIMIT 5;')
    return res.fetchall()


if __name__ == '__main__':
    print(get_last_five_users())
