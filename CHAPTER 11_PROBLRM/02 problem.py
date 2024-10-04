# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class animal:
    pass


class pets:
    pass



class dog(pets):
    @staticmethod
    def bark():
        print("boow bow")


d =dog()

d.bark()