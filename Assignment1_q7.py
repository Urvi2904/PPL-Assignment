#Find Armstrong Numbers in the given range.

def getdigits(number) :
	digits = [int(x) for x in str(number)]
	return digits

start = int(input("Enter lower limit of range(included) : "))
end = int(input("Enter upper limit of range(excluded) : "))
numbers = list(range(start, end))
print("Armstrong numbers : \n")
for number in numbers :
	digits = getdigits(number)
	sum = 0
	for digit in digits :
		sum += (digit ** 3)
	if sum == number :
		print(number)
	else :
		continue 
