def wordcount(message):
    word=0
    i=0
    while i<len(message):
        if message[i]==" ":
            word+=1
        i+1
    return word
message(input("Enter message - "))
print("number of words are = ", (wordcount))