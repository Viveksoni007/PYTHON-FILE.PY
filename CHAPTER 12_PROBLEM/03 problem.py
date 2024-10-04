# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input('ENTER THE TABLE NUMBER '))

table = [n*i for i in range(1,11)]
with open ("table.txt","a")as f:
    f.write(f"Table of This {n}:{str (table)}\n")

