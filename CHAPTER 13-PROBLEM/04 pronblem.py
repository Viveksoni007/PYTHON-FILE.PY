def devisible59(n):
    if (n%5 == 0):
        return True
    return False



a = [1,12,56,565,66555,845,56565,]
f = list(filter(devisible59,a))

print(f)