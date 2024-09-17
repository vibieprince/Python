import sqlite3
conn=sqlite3.connect('sqlite.db')
ins='''
    insert into students(st_id,st_fees) VALUES 
    (5,4000)
    '''
conn.execute(ins)
conn.commit()
conn.close()
