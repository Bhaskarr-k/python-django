import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_learning")
cur=conn.cursor()
cur.execute("delete from employee where empaddress='bnglr'")
conn.commit()
conn.close()