from functools import reduce
#map example

l = [1,2,3,4,5,6]

square =lambda x: x*x

sqlist = map(square,l)
print(list(sqlist))

# filter example
def even (n):
    if (n%2 ==0):
        return True
    return False


onlyeven =filter(even,l)
print(list(onlyeven))

# Reduce function Example

def sum(a, b):
    return a + b

print(reduce(sum,l))