1.
# Write a program using functions to find greatest of three numbers

a = 1
b = 2
c = 3

def gratest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c
    


# a = 1
# b = 2
# c = 3

a= int(input("Enter the number IS ;"))
b= int(input("Enter the number IS ;"))
c= int(input("Enter the number IS ;"))


print(gratest(a,b,c))