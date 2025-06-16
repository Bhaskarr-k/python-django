# def function():
#     print('user defined functions')
# function()
# function()

# def sample():
#     # return
#     print('sample function')
#     print('second')
#     print('thrid')
#     return
#     print('fourth')
# r=sample()
# print(f'r:{r}')


# def add_numbers(a,b):
#     return a+b
# num1=5
# num2=10
# result=add_numbers(num1,num2)
# print(result)

# def xyz(a,b):
#     print(f'a:{a}')
#     print(f'b:{b}')
# n1=10
# n2=20
# r=xyz(n1,n2)
# print(f'r:{r}')

# def details(name,age,id):
#     print(f'name:{name}')
#     print(f'age:{age}')
#     print(f'id:{id}')
# details('bhaskar',24,100)

# x=[10,20,30]
# r=list(map(lambda n:n//2,x))
# print(r)


# x=[6,15,21]
# z=list(map(lambda n:n//3,x))
# print(z)


# add=lambda x,y,z:x+y+z
# print(add(5,5,6))

def fun():
    print(f'global space:{x}')
x=30
fun()
print(f'')