# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?

class DEMO:
    a=4

o =DEMO()
print(o.a) # prints the class atribute because instance attribute is not present 
o.a =0 #instance atttibute is set
print(o.a)#prints the instance the attributes because instance attribute is present

print(DEMO.a) # prints the classs attributes 