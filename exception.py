try:
    """
    the code which can give raise to an exception is written here
    """
    a = "100"
    b = int(a)
    print("i am here")
except:
    print("exception caught")


# catching specific exception
try:
    a = 5
    b = 6
    c = 8
    print("c=",c)
    print("b=",b)
except zerodivisionerror:
    print("zero division error")


# catching specific exception
try:
    a = 100
    b = 20
    c = a/b
    print("{} / {} = {}".format(a,b,c))
except ZeroDivisionError:
    print("divisoin by zero is not possible")