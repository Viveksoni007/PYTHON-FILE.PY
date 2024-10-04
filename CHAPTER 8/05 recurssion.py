'''
factrial (1)=   1
factrial (2)=  2 X 1
factrial (3)=  3 X 2 X 1
factrial (4)=  4 x 3 X 2 X 1
factrial (5)=  5 X 4 x 3 X 2 X 1

factoirial (n)= n X n-1 X ..........3X 2X 1

factorial(n)=  N*faxtorial (n-1)

'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter The Number is :"))
print(f"the factorial of this is {factorial (n)} :")
