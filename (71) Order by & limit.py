import pymysql as mq
mysql=mq.connect(host="localhost",user="root",password="pass",database="state")
mycursor=mysql.cursor()
print(("{:<14} {:<18} {:<20}").format("state_id","state_name","country_id"))
try:
    sql="select * from states order by state_id ASC limit 4,2"
    mycursor.execute(sql)
    sdata=mycursor.fetchall()
    for s in sdata:
        print(("{:<15}{:<20}{:<20}").format(s[0],s[1],s[2]))
except:
    print(" Database Error...")
