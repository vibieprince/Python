import pymysql as m
o=m.connect(host="localhost",user="root",password="paas",database="school")
my=o.cursor()
print(("{:<15}{:<20}{:<20}").format("student ID","Student Name","Student Class","Student Email"))
try:
    name=input("Enter the Student Name :- ")
    classname=input("Enter Student's class :- ")
    sql="Select * from student where st_name like '%"+name+"%' or st_class = '"+classname+"'"
    my.execute(sql)
    sdata=my.fetchall()
    for s in sdata:
        print(("{:<15}{:<20}{:<20}").format(s[0],s[1],s[2],s[3]))
except:
    print('ERROR 404')
