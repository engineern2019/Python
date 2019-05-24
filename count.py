Cost=int(input("Enter Cost = "))
Amount=int(input("Enter Balance = "))
Balance=Amount-Cost
print("Owing = ", Balance)
fifty=int(Balance/50)
if fifty>0:
	print("£50 = ", fifty)
	Balance=Balance%50
twenty=int(Balance/20)
if twenty>0:
	print("£20 = ", twenty)
	Balance=Balance%20
ten=int(Balance/10)
if ten>0:
	print("£10 = ", ten)
	Balance=Balance%10
five=int(Balance/5)
if five>0:
	print("£5 = ", five)
	Balance=Balance%5
two=int(Balance/2)
if two>0:
	print("£2 = ", two)
	Balance=Balance%2
one=int(Balance/1)
if one>0:
	print("£1 = ", one)
	Balance=Balance%1