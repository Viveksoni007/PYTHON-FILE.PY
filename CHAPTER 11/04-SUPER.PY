class employee:
    def __init__(self):
        print("constructer of the employee")
    a=1


class programmer(employee):
    def __init__(self):
        print("contructer of the programmer")
    b=2

class manager(programmer):
    def __init__(self):
        super().__init__()
        print("constructer of the manager")
    c=3

    # o= employee()
    # print(o.a) # print the a attribute


# o = programmer()
# print(o.a,o.b)


o = manager()
print(o.a,o.b,o.c)