# import turtle
# turtle.bgcolor("Black")
#
# squary = turtle.Turtle()
# squary.speed(25)
# squary.pencolor("red")
# for i in range(400):
#     squary.forward(i)
#     squary.left(50)


import pymysql
def mysqlconnect():
    conn=pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = 'pass',
        db ='college'
        )
    cur=conn.cursor()

    try:
        db="create database state"
        cur.execute(db)
        print("database created")
    except:
           print("database error..")