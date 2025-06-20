import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Bhaskar",
  database="python_learning"
)

mycursor = mydb.cursor()

q = "SELECT * FROM employee ORDER BY empid"

mycursor.execute(q)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)