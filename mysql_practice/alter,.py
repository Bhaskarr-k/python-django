import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_learning")
cur=conn.cursor()
cur.execute("alter table employee add section varchar(20) DEFAULT 'A'")
conn.commit()
conn.close()