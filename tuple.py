x=(1,2,3,4,"basu","python")
print(x)
# tuple with mixed data types
x=(1,2,3,4,"basu","python")
print(x)
# nested tuple
tuple=("basu",[1,2,3],(5,67))
print(tuple)
# tuple unpacking
tuple1=101,"basu",2000.00,"developer"
empid,empname,empsalary, designation=tuple1
print(tuple1)
print(empid)
print(empname)
print(empsalary)
print(designation)
# accessing elements with tuple
tuple1=(1,2,2,5,7,8,'basu','bangalore')
print(tuple1)
print(tuple1[2])
print(tuple1[4])
# slicing
tuple1=(1,2,2,5,7,8,'basu','bangalore')
print(tuple1)
print(tuple1[1:4])
# concatinating
tuple1=(12,2,4,5,'basu')
tuple2=(5,6,7,8,'bhaskar')
print(tuple1)
print(tuple2)
print(tuple1 + tuple2)