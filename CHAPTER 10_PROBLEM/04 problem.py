# Add a static method in problem 2, to greet the user with hello.

class calculator:
    def __init__(self, n ):
        self.n =n


    def squre(self):
        print(f"the squre is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squreroot(self):
        print(f"the squre root is {self.n**1/2}")
    @staticmethod
    def hello():
        print("hello there !")    




# a =int(input("enter The number is "))
# print(a.squre,a.cube,a.squreroot)

a= calculator(4)
a.hello()
a.squre()
a.cube()
a.squreroot()