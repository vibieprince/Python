import sqlite3
conn=sqlite3.connect("sqlite.db")
print("STUDENT ID","STUDENT NAME","STUDENT FEES")
#data=conn.execute("SELECT * FROM students as f inner join student as s on f.st_id=s.st_id")
data=conn.execute("SELECT f.st_id,s.st_name,f.st_fees FROM students as f left join student as s on f.st_id=s.st_id")

for a in data:
    print(a[0],a[1],a[2])
conn.close()

