number=[]
while True:
    num=int(input("enter any number = "))
    if num==0:
        break
    else:
        number.append(num)

Highest = number[0]
i=1
while i<len(number):
    if number[i]>Highest:
        Highest=number[i]
    i=1+1
print("This ", Highest)