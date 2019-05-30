f=0
msg=input("enter any message - ")
word=input("what are you looking for? ")
i=0
while i<len(msg):
    if msg[i:i+len(word)]==word:
        f=f+1
        i=i+len(word)-1
    i=i+1
print("There is", f, "--", word, "-- in the message")