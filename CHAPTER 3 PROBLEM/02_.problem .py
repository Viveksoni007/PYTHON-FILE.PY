# Write a program to fill in a letter template given below with name and date.


letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''


print(letter.replace("<|Name|>","vivek").replace("<|Date|>","02september2024"))