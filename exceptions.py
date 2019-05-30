try:
    no1=int(input("enter no = "))
    no2=int(input("enter no = "))
    result=no1/no2
    print("result is = ",result)
except ValueError:
    print("enter digits only")
except ZeroDivisionError:
    print("cannot devide by 0")
finally:
    print("try again")