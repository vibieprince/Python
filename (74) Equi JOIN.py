import pymysql as m
mysql=m.connect(host="localhost",user="root",password="pass",database="state")
c=mysql.cursor()
print(("{:<15}{:<20}{:<20}").format("State ID","State Name","Country ID"))
try:
    sql="select states.state_id,states.state_name,country.country_id from states,country where states.state_id=country.state_id"
    c.execute(sql)
    sdata=c.fetchall()
    for s in sdata:
        print(("{:<15}{:<20}{:<20}").format(s[0],s[1],s[2]))
except:
    print("databse error")
