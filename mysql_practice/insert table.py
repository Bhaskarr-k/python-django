# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_mysql")
# cur=conn.cursor()
# q="insert into students(rollno,sname,branch)values(%s,%s,%s)"
# v=[(101,"ram","ece"),(102,"basu","eee"),(103,"pawan","ai")]
# try:
#     cur.executemany(q,v)
#     conn.commit()
# except:
#     conn.rollback()
# conn.close()


# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="learn")
# c=conn.cursor()
# q="insert into marks(telugu,maths,english,science)values(%s,%s,%s,%s)"
# v=(45,67,68)
# try:
#     c.execute(q,v)
#     conn.commit()
# except:
#     conn.rollback()
# conn.close()

import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_learning")
c=conn.cursor()
q="insert into employee(empname,empid,empaddress)values(%s,%s,%s)"
v=[("Basu",102,"bnglr"),("ram",201,"tpt"),("siva",105,"kadapa"),("charan",205,"piler"),("pawan",20,"rayachoty"),("kalyan",25,"nagiri")]
try:
    c.executemany(q,v)
    conn.commit()
except:
    conn.rollback()
conn.close()
