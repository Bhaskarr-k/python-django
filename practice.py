# x=50
# print(x)
# print(type(x))

# y=10.0
# print(y)
# print(type(y))

# x='basu',"bhaskar",'basu'
# print(x)
# print(type(x))

# define tuple
# x=[10,]
# print(x)

# y={}
# y[20]='bhaskar'
# y[30]='basu'

# print(y)

# x='BHaskar@123'
# y=x.split('a')
# print(y)

# x='bhaskar'
# course='python'
# print(f'my name is {x} and my course is {course}')

# x=[1,2,34,2,1,2,'basu','basu']
# r=x.append(5)
# print(f'r:{r}')
# print(f'x:{x}')
# e=x.insert(2,'bhaskar')
# print(f'e:{e}')
# print(f'x:{x}')
# b=x.extend('abc')
# print(f'b:{b}')
# print(f'x:{x}')
# v=x.remove(2)
# print(f'v:{v}')
# print(f'x:{x}')
# list1=[1,2,3]
# list2=[4,5,6]
# list1.extend(list2)
# print(list1)

# list1=[1,2,3,4,5,6,7]
# list1.remove(1)
# print(list1)

# x=[1,2,3,4,5,6]
# r=x.pop()
# print(f'r:{r}')
# print(f'x:{x}')

# numbers = [5,3,1,7,2]
# numbers.sort()
# print(numbers)

# x=['i', 'am','bhaskar']
# print('@'.join(x))
# print(x)

# x={1,2,3,4}
# y={2,3,5}
# r=x.difference(y)
# print(r)

# x={1:"basu",2:"bhaskar",'c':"siva"}
# print(x.get('c'))

# age=int(input('enter your age'))

# if age>=5:
#     print("you are eligible")
# else:
#     print("you are not eligible")

# for x in range(1,100):
#     print(x)

# x='string'
# for ind  in range(0,len(x)):
#    print(ind)

# i = 1  # starting value

# while i <= 1:
#     print(i)
#     i += 1  # increment by 1


# for i in range(1,11):

# n=5
# for x in range(n):
#     for y in range(n):
#         if x%2==0:
#             print('*', end='')
#         else:
#             print('#', end='')
#     print()


# n=5
# col=1
# for x in range(n):
#     for y in range(col):
#         print('*', end='')
#     print()
#     col=col+1

# prime numbers program
# n=3
# t=0
# if n<=1:
#     t=1
# for j in range(2,n):
#     if n%j==0:
#         t=1
#         break
# if t==0:
#     print('prime')
# else:
#     print('not prime')

# # even or odd
# n=8
# if n%2==0:
#     print('even')
# else:
#     print('odd')


# n=5
# t=1
# for j in range(1,n+1):
#     t=t*j
# print(t)

# s="my name is bhaskar"
# print(s[2:7])
# print(s[3:])
# print(s[:7])
# print(s[:-1])
# print(s[2:8:3])

# remove duplicates in a string
# x="my name is my course name is python"
# t=""
# for z in x:
#         if z not in t:
#                 t=t+z
#         print(t)


# write a program to number of times each charecter is repeated in given string

# x="bhaskar basu"
# t={}
# for a in x:
#     if a not in t:
#         t[a]=1
#     else:
#         t[a]+=1
# for k,v in t.items():
#     print(f'{k}={k}')

x="bhaskar basu"
l=x.split() [::-1]
print(''.join(l))


