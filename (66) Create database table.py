import pymysql as mq
conn=mq.connect( host="localhost", user="root",database="state")
#Table school (st_id,st_name,st_class,st_email)
cur=conn.cursor()
t="create table country(state_id VARCHAR(30) ,state_name VARCHAR(40),country_id VARCHAR(10))"
cur.execute(t)
try:
    t="create database state"
    cur.execute(t)
except:
       print("database error")

