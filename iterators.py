list=[32,45,75,33]
list=iter(list)
print(next(list))
print(next(list))
print(next(list))


# create cusotm iteraor

class pow_of_two:
    def _init_(self, max = 0):
    self.max = max