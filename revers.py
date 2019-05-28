found=0
msg=input("enter any message ")
char=input("what letter are you looking for? ")
i=0
while i<len(msg):
    if msg[i]==char:
        found = found +1
    i=i+1
print=found