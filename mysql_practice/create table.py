# import mysql.connector
# conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python_mysql")
# cur=conn.cursor()
# cur.execute("create table students(rollno int not null primary key,sname varchar(20) not null,branch varchar(10) not null)")
# conn.close()


import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="learn")
c=conn.cursor()
c.execute("create table marks(telugu int(20),english int(20),maths int(20),science int(20))")
conn.close()