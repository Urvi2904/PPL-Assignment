#Find the first 10 pairs of amicable numbers. 

def findDivisors(num) :
	divisors = []
	root = int(num ** 0.5)
	#excluding 1 to avoid pair num
	for i in range(2, root + 1) :
		if num % i == 0 :
			divisors.append(i)
			divisors.append(int(num / i))
	return divisors

def findDivSum(num) :
	divisors = findDivisors(num)
	sum = 0
	for divisor in divisors :
		sum += divisor
	#compensate for excluded 1
	sum += 1
	return sum

count = 0
a = 200
print("First 10 pairs of amicable numbers :")
while count < 10 :
	a += 1
	a_sum = findDivSum(a)
	if a_sum > a :
		b_sum = findDivSum(a_sum)
		if b_sum == a :
			print(a, ", ", a_sum)
			count += 1
	else :
		continue
