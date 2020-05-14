#Find the first 10 harmonic divisor numbers. 

import statistics
import math

def findDivisors(num) :
        divisors = []
        root = int(num ** 0.5)
        for i in range(1, root + 1) :
                if num % i == 0 :
                        divisors.append(i)
                        divisors.append(int(num / i))
        return divisors

def findHarmonicMean(divisors) :
	reciprocals = []
	for divisor in divisors :
		reciprocals.append(float(1.0 / float(divisor)))
	am = float(statistics.mean(reciprocals))
	hm = float(1.0 / am)
	return hm

num = 0
count = 0
print("First 10 harmonic divisor numbers :\n")
while count < 10 :
	num += 1
	divisors = findDivisors(num)
	hm = findHarmonicMean(divisors)
	if hm == math.floor(hm) :
		print(num)
		count += 1
	else : 
		continue
