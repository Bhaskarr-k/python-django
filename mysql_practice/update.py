import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_learning")
c=conn.cursor()
c.execute("update employee set empid=106 where empname='basu'")
conn.commit()
conn.close()         
