def make_decorated(func):
    def inner_function():
        print("i got decorated")
        func()
    return inner_function
def simple_func():
    print("i am a simple function")

decor = make_decorated(simple_func)
decor()