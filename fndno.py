def change(number):
    i=0
    letters=""
    while i<len(number):
        ascii= ord(number[i])
        if ascii=>65 and ascii<=90:
            letters+=chr(ascii+32)
            else:
                if ascii>=97 and ascii<=122:
                    else:
                        if ascii>=48 and ascii<=57:
                            letters+=str(chr(ascii)*2)
                            else:
                                letters+=chr(ascii)
            i+=1
            return letters
msg=input("enter any number = ")
change(msg)