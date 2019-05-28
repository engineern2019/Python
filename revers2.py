msg=input("enter a message - ")
word=" "
i=len(msg)-1
while i>=0:
    if word[i]==" ":
        print(word)
        word=""
    else:
        word=msg[i]+word
    i=i+1
print(word)