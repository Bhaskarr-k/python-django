# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar")
# c=conn.cursor()
# c.execute("create database learning")
# for i in c:
#     print(i)


# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",)
# c=conn.cursor()
# c.execute("create database learn")
# for i in c:
#     print(i)

import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar")
cur=conn.cursor()
cur.execute("create database python_learning")
for i in cur:
    print(i)