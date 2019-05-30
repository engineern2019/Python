file_read=open("commute.txt", "r")
file_write=open("commute2.txt", "w")
for data in file_read:
    for ch in data:
        if ch==" ":
            print("*",end="")
        else:
            print(ch,end+"")