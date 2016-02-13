import sqlite3

def sendcommand():
    conn = sqlite3.connect('data-dev.sqlite3')
    cur = conn.cursor()
    cur.execute("UPDATE command SET command='open' WHERE Id=1")
    conn.commit()
