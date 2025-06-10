# iterating a string using for loop
h_letters=[]
for letter in 'human':
    h_letters.append(letter)
    print(h_letters)

# using comprehension
h_letters=[letter for letter in 'human']
print(h_letters)

# nested if with list comprehension
num_list=[y for y in range(100) if y%2==0 if y%5==0]
print(num_list)