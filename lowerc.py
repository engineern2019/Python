Alpha=input("Enter any charecter - ")
if ord(Alpha)>=65 and ord(Alpha)<=90:
    print(chr(ord(Alpha)+32))
else:
    if ord(Alpha)>=97 and ord(Alpha)<=122:
        print(chr(ord(Alpha)-32))
    else:
        if ord(Alpha)>=48 and ord(Alpha)<=57:
            print("Digit")
        else:
            print("Any Other Charecter")