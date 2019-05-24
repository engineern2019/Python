name=input("Please enter name - ")
salary=int(input("Please enter your salary - "))
if salary>2000:
	tax=salary*25/100
else:
	tax=salary*15/100
netsalary=salary-tax
print("_____________________")
print("Name - ", name)
print("Salary - ", salary)
print("Tax - ", tax)
print("Net Salary", netsalary)
print("_____________________")