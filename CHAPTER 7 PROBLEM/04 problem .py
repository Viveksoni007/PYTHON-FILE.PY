# Write a program to find whether a given number is prime or not.

n = int(input("enter a number is :"))

for i in range(2,n):
    if(n%i)==0:
        print("number is not prime number")
        break

else:
    print("the give numver is prime number")    
