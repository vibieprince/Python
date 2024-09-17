import pymysql as m
k=m.connect(host="localhost",user="root",password="pass",database="school")
x=k.cursor()
p=input("Enter the student id:- ")
c=input("Enter the class :- ")
n=input("Enter the student name :- ")
e=input("Enter the email id:- ")

sql="UPDATE student set st_name=%s,st_class=%s, st_email=%s where st_id=%s"
data=(n,c,e,p)
try:
    x.execute(sql,data)
    k.commit()
    print("corresponding database is updated")
except:
    print("databse error")