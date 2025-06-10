a=2
print('(id(2)) = ',id(2))

a=3
print('(id(3)) = ',id(3))


# scope

def outer_function():
    global a
    a=20

    def inner_function():
        global a
        a =30
        print('a= ',a)

    inner_function
    print('a =', a)

a=10
print('a =',a)
outer_function()
print('a = ',a)