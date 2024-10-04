import random
n =random.randint(1,100)
a=-1
guesses=0
while(a !=n):
    a = int(input("guess the number : "))
    if(a>n):
        print("lower number please")
        guesses +=1
    # else:
    #     print("Higher number please")
    elif(a<n):
        print("Higher number please")
        guesses +=1

    

print(f"you have gussed the number{n} correctly in {guesses} attempy")