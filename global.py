def funct1():
    x = 20

    def funct2():
        global x
        x = 25


    print("before calling funct2: ", x)
    print("calling funct2 now")
    funct2()
    print("after calling funct2:", x)
funct1()
print("x in main : ", x)