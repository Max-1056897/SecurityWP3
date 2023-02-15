import sqlite3
sqlite3.connect('aanmeldingstool')

conn = sqlite3.connect('aanmeldingstool') 
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS users
          ([user_id] INTEGER PRIMARY KEY, [username] TEXT, [password] TEXT)
          ''')
          
conn.commit()