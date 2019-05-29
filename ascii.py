Alpha=input("Enter any charecter")
if ord(Alpha)>=65 and ord(Alpha)<=90:
    print("Upper Case")
else:
    if ord(Alpha)>=97 and ord(Alpha)<=122:
        print("Lower Case")
    else:
        if ord(Alpha)>=48 and ord(Alpha)<=57:
            print("Digit")
        else:
            print("Any Other Charecter")