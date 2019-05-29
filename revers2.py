msg=input("enter a message - ")
word=" "
i=0
i=len(msg)-1
while i>=1:
    if msg[i]==" ":
        print(word)
        word=" "
    else:
        word=word+msg[i]
    i=i+1
print(word)