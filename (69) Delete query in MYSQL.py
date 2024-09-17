import pymysql as m
mysql=m.connect(host="localhost",user="root",password="pass",database="state")
x=mysql.cursor()
k=int(input("Enter the student id :-"))
sql="DELETE FROM country where state_id=%s"
try:
    x.execute(sql,k)
    mysql.commit()
    print("student's data DELETED")
except:
    print("database error")
