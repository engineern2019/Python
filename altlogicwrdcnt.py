def countletters(message,letters):
a=0
count=0
while a<len(message):
    if (message[a].upper)==letters:
        count+=1
        a+=1
    if count>0:
        print(letters," = ",count)
        msg=input("enter any letters or words")
        c=65
    while c<=90:
        countletters(msg,chr(c))
        c+=1