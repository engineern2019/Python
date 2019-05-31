def repo (day):
    if day==1:
        def fun(a,b):
            c=a+b
            print("RESULT OF ADDITION = ", c )
    if day==2:
        def fun(a,b):
            c=a-b
            print("The result of subtraction =", c)
    return fun
delta=repo(2)
delta(5,2)