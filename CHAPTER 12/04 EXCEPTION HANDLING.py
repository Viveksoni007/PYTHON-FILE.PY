

try:
    a=int(input("Hey,  Enter the number is :"))
    print(a)

except ValueError as v:
    print("Hey what you doing?")
    print(v)
except Exception as e:
    print(e)


print("Thank you dear!")