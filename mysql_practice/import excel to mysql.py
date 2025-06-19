import mysql.connector
import xlrd
conn=mysql.connector.connect(host="localhost",user="root",password="Bhaskar",database="python")
curr=conn.cursor()
loc=("C:\\Users\\LENOVO\\Desktop\\csv files\\student.xlsx")
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0)
sheet.cell_value(0,0)
for i in range(1,21):
    print(sheet.row_values(i))
conn.close()
