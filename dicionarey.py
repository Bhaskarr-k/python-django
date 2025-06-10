new_dict={1:"hello",2:"world",3:"hi"}
print(new_dict)
print(new_dict[1])
print(new_dict[2])
print(new_dict[3])

# updating a value
new_dict[1]="hi"
print(new_dict)


# nested dictionarey
people={1:{'name':'john','age':27},
        2:{'name':'basu', 'age':24}}
print(people)

# Accessing elements of dictionarey
print(people[1]['name'])
print(people[1]['age'])
print(people[2]['age'])

# Addineg elements
people[2]['name']='bhaskar'
print(people)
