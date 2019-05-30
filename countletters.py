#wordcount using the list works with lower case as well.

capletter=[0]*26
letter=[0]*26
message=input("Please imput any letter - - ")
i=0
while i<len(message):
    if ord(message[i])>=65 and ord(message[i])<=90:
        capletter[ord(message[i])-65]+=1
    if ord(message[i])>=97 and ord(message[i])<=122:
        letter[ord(message[i])-97]+=1
    i+=1
a=0
while a<=25:
    if capletter[a]>0:
        print(chr(a+65)," = ", letter[a])
    
    if letter[a]>0:
        print(chr(a+97)," = ", capletter[a])
    
    a+=1