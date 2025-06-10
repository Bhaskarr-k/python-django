arr=[10,20,20,30,50,'basu']
print(arr)
# accessing an array
print(arr[0])
print(arr[-1])
# finding length
fruits=['sapota','mango','apple','cherry']
print(fruits)
arr_fruits=len(fruits)
print(arr_fruits)
# adding a element using append
fruits=['sapota','mango','apple','cherry']
fruits.append('watermelon')
print(fruits)
# removing element from an array
fruits=['sapota','mango','apple','cherry']
print(fruits)
del fruits[2]
print(fruits)
fruits.remove('sapota')
print(fruits)
# modifying array using indexing
fruits=['sapota','mango','apple','cherry']
fruits[1]='muskmilon'
print(fruits)
# concatinating two operators using + operator
arr1=[1,2,3]
arr1=arr1+ [4,5,6]
print(arr1)
# repeting element in array

repeat= ["a"]
repeat = repeat * 5
print(repeat)

# slicing an array
fruits=['apple','banana','sapota','watermelon']
print(fruits)
print(fruits[1:4])
print(fruits[ :3])
print(fruits[-3:-1])

# declaring and defining multidimensional array
arr1=[[1,2],[3,4],[6,7],[8,9]]
print(arr1)
print(arr1[0])
print(arr1[1])
print(arr1[2][1])