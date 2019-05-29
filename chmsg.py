def change(message):
    i=0
    newmessage=""
    while i<len(message):
        if ord(message[i])>=65 and ord(message[i])<=90:
            newmessage+=chr(ord(message[i])+32)
        else:
            if ord(message[i])>=97 and ord(message[i])<=122:
                newmessage+=chr(ord(message[i])-32)
        i+=1
    return newmessage

msg=input("Provide Message")
print(change(msg))