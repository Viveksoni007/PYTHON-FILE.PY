from functools import reduce

a= [1,2,66,445,9966,999,55,63]

def grater(a,b):
    if(a>b):
        return a
    return b


print(reduce(grater,a))