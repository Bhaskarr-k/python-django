# global and local variabls names with difrent Name
x='global'

def funct1():
    global x
    y='local'
    x=x*2
    print(x)
    print(y)

print("glbal x= ", x)
funct1()
print("global x= ",x)


# global and local variables same name
a =5
def funct2():
    a=10
    print("local a: ",a)
print("global a:",a)
funct2()
print("global a:",a)

# non local variable
def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:",x)
outer()