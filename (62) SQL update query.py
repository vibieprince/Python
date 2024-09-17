import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
             update student set st_name="RAM" where st_id=9
             ''')
conn.commit()
conn.close()