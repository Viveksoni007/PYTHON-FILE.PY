# Repeat program 4 for a list of such words to be censored.

words =["donkey", "ganda ","harry","vivek","good"]

with open ("file1.txt","r")as f:
    content = f.read()

for word in words:
    content=content.replace(word , "#"*len(words))

with open("file1.txt","w")as f:
    f.write(content)