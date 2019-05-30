#program to replace one charecter with a * in the commute2.txt file.
file_read=open("commute.txt", "r")
file_write=open("commute2.txt", "w")
for data in file_read:
    for ch in data:
        if ch=="y":
            print("*",file=file_write,end="")
        else:
            print(ch,file=file_write,end="")