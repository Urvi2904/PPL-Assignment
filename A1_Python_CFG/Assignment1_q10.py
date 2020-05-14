#Find the first 10 numbers from geometric series. 

a = float(input("Enter the first number in the series.\n"))
r = float(input("Enter the common ratio.\n"))
i = 10
print("First 10 terms of geometric series : \n")
while i :
	print(a)
	a = a * r
	i -= 1	
