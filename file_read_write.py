file_read=open("commute.txt", "r")
file_write=open("commute2.txt", "w")
for data in file_read:
    print(data,file=file_write)