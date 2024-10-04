a=89


def fun():
    global a   # global word change kar deta function ke variable ko change kar deta 
    a=3
    print(a)

fun()
print(a)