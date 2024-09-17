import pymysql as mq
#server connection
mysql=mq.connect(host="localhost",user="root",password="pass",database="school")
mycursor=mysql.cursor()
print(("{:<15} {:<20}").format("student id", "student Name"))

try:
    sql="select st_id,st_name from student where st_id=2"
    mycursor.execute(sql)
    sdata=mycursor.fetchone()
    print(("{:<15} {:<20}").format(sdata[0],sdata[1]))
except:
    print("database error")

