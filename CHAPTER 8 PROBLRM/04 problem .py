# Write a recursive function to calculate the sum of first n natural numbers.

'''
summ(1)= 1
summ(2)= 1+2
summ(3)= 1+2+3
summ(4)= 1+2+3+4
summ(5)= 1+2+3+4+5

sum(n )=  1 + 2+ 3 + ......n
sum (n )= sum(n-1) +n

'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) +n


print(sum(4))
