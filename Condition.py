no=int(input("Please enter number = "))
if no>1000:
	print("B")
	if no>2000:
		print("C")
	else:
		print("F")
	print("2")
else:
	if no<1000:
		print("A")
		if no>500:
			print("D")
		else:
			print("E")
	print("1")
print("3")