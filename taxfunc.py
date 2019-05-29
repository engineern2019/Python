def tax(salary):
    if salary>1500:
        tax=salary*21/100
    else:
        tax=salary*15/100
    return tax

salary=int(input("Enter Salary"))
print("Your tax", tax(salary))
print("Net", (salary-tax(salary)))