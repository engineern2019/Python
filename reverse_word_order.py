#amended the 

def rev(word):
    newword=""
    x=len(word)-1
    while x>=0:
        newword+=word[x]
        x-=1
    return newword
message=input("enter message - -")
newmessage=" "
word=" "
for ch in message:
    if ch ==" ":
        newmessage+=(rev(word)+" ")
        word=""
    else:
        word+=ch
print(newmessage,rev(word))