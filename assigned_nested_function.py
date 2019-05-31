#Below subract and addition functions have been assigned to operations to.

def operations(f,a,b):
    f(a,b)


def subtraction(x,y):
        c=x-y
        print("Subtraction result =", c)


def addition(a,b):
        c=a+b
        print("Addition result =", c)
        
operations(addition,80,20)
operations(subtraction,50,10)