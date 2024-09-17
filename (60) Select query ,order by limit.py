import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM Student")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
for n in data:
    print(n,[0],"     ",n[1],"    ",n[2],"    ",n[3])

import sqlite3
conn=sqlite3.connect("sqlite.db")
data=conn.execute("SELECT * FROM Student limit 2,2")
print("STUDENT ID","STUDENT NAME","STUDENT CLASS","STUDENT EMAIL")
for n in data:
    print(n,[0],"     ",n[1],"    ",n[2],"    ",n[3])
