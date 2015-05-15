import sqlite3
conn = sqlite3.connect("database.db")
c = conn.cursor()
c.execute('''CREATE TABLE users (name text, address text, password text)''')
c.execute('''CREATE TABLE admins (name text, address text, password text)''')
c.execute('''CREATE TABLE temps (name text, address text)''')
conn.commit()
conn.close()
