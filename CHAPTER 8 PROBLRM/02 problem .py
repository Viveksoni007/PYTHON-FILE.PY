# Write a python program using function to convert Celsius to Fahrenheit.

# TODO: formula of forren hieght    c/5 = f-32/9

f = int(input("enter the temprature  :"))
c = 5*(f-32)/9

print(c)


#function se solve kiya gaya hai this problem 
def f_to_c(f):
    return  5*(f-32)/9

f = int(input("enter the temprature  :"))

# print(f_to_c(f))   # yeah bhi ek trika hai iske alwa  f ko srting ban ke kar sakte hai 
c = f_to_c(f)
print(f"{round(c,2)} °C")