import pymysql
mysql=pymysql.connect(database="state")
mycursor=mysql.cursor()

#st_id,st_name,st_class,st_email
# ins="INSERT INTO student(st_name,st_class,st_email) values (%s,%s,%s)"
# t=("ravi","12th","ravi@gmail.com")
# mycursor.execute(ins,t)
# mysql.commit()
# print("Data inserted")

try:
    ins="INSERT INTO country(state_id,state_name,country_id) values (%s,%s,%s)"
    t=[("5","Maharashtra","+91"),("6","Sikkim","+91")]
    mycursor.executemany(ins,t)
    mysql.commit()
    print("Data inserted")
except:
    print("database already exist")

