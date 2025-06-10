# function with no return statement
def hello1():
    print("hello how are you")
hello1

# function with return statement

def hello2():
    """ this is
    a  
    multi line string"""
    return "hello, hai"
hello1()
print(hello2())
print(hello2.__doc__)





# default arguments

def findmax(a,b):
    if a>b:
        return a
    else:
        return b
    
print(" max number between 10 and 20 is ",findmax(10,20))

# function with default parameter
def hello(name, msg = ", how are you?"):
    print("hello ", name, msg)
hello("basu",", hava anice day")
hello("basu")