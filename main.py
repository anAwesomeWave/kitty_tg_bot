from core import bot
import sqlite3

from settings import DB_PATH


def run_app():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users(
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL,
                        time DATETIME
                    );
                    ''')

    con.commit()
    bot.serve()


run_app()
