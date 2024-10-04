class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class vlaue of a is : {cls.a}")


e = employee()
e.a=95


e.show()