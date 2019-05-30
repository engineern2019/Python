#wordcount using the list(will only work with capital letters)

letter=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
message=input("Please imput any letter - - ")
a=0
while a<len(message):
    letter[ord(message[a])-65]+=1
    a+=1
a=0
while a<=25:
    if letter[a]>0:
        print(chr(a+65)," = ", letter[a])
    a+=1