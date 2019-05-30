def rev(x):
    x=x[::-1]
    for i in range(len(x)):
        if x[i] == " ":
            x=x[::-1]
            continue
        print (x)