import pymysql as m
k=m.connect(host="localhost",user="root",password="pass",database="state")
c=k.cursor()
print(("{:<15}{:<20}{:<20}").format("State ID","State Name","Country ID"))
try:
    sql="Select states.state_id,states.state_name,country.country_id from states left join country on states.state_id=country.state_id"
    c.execute(sql)
    sdata=c.fetchall()
    for s in sdata:
        print(("{:<15}{:<20}{:<20}").format(s[0],s[1],s[2]))
except:
    print("database error")
print()
print()
#Right Join
import pymysql as m
k=m.connect(host="localhost",user="root",password="pass",database="state")
c=k.cursor()
print(("{:<15}{:<20}{:<20}").format("State ID","State Name","Country ID"))
try:
    sql="Select * from country right join states on country.state_id=states.state_id"
    c.execute(sql)
    sdata=c.fetchall()
    for s in sdata:
        print(("{:<15}{:<20}{:<20}").format(s[0],s[1],s[2]))
except:
    print("database error")


