import random
'''
1 for snake
-1 for water 
0 for gun 


'''

computer =random.choice([-1, 0, 1])
youstr = input("enter your choice :")
youDict= {"s":1,"w":-1, "g": 0}
reveraedict={1:"snake ",-1:"water",0:"gun"}
you= youDict[youstr]


# by now we have 2 number {variable},and you and computer 

print(f"you chose {reveraedict[you]}\ncompuert chose {reveraedict[computer]}")

if(computer==you):
    print("its draw")

else:
    if(computer==-1 and you ==1):
        print("you win")

    elif(computer==-1 and you == 0):
        print("You Lose!")    

    elif(computer==1 and you == -1):
        print("You Lose!")    

    elif(computer==1 and you == 0):
        print("You win")    

    elif(computer==0 and you == -1):
        print("You Win")    

    elif(computer==0 and you == 1):
        print("You Lose!")

    else:
        print("somethings went worng")

    
