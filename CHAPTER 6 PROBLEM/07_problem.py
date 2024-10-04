# Write a program to find out whether a given post is talking about “Harry” or not.


# post = "harry is bhai is good harry is very good GRAET"


post = input("Enter this post ")

if("harry ".lower() in post.lower()):
    print("this poster is taking about harry ")

else:
    print("this poster is  not taking about harry ")
