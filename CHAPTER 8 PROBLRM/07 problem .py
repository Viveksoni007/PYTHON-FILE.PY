# Write a python function to remove a given word from a list ad strip it at the same time.



# this function kouse kar ke lo list me itemko hatna hai hata skate hai 
# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l



#this function use ksre ek personal ko me ek (an )jaise ko srtip kar sakte hai ok 


def rem(l,word):
    n=[]
    for item in l:
        if not(item==word):
            n.append(item.strip(word))
    return n



l= [ "harry ",  "vivek", "Arti", "Shubham" ,"an" "Rohan"]



print(rem(l, "an"))