#Computers usually solve square systems of linear equations using the LU decomposition. Write a program to compute LU decomposition. 

mat = []
n = int(input("Enter size of matrix.\n"))
print("Enter matrix elements in row major order.\n")
i = 0
j = 0
for i in range(n) :
	a = []
	for j in range(n) :
		a.append(int(input()))
	mat.append(a)
	

#initializing upper and lower triangular matrices.
upper = [[0 for i in range(n)] for j in range(n)]
lower = [[0 for i in range(n)] for j in range(n)]

i = 0
j = 0
k = 0
for i in range(n) :
	#Upper decomposition
	for k in range(i, n) :
		#sum of products lower[i][j]*upper[j][k]
		sum = 0
		for j in range(i) :
			sum += (lower[i][j] * upper[j][k])

		upper[i][k] = mat[i][k] - sum

	#Lower decomposition
	for k in range(i, n) :
		if i == k :
			#diag set to 1
			lower[i][i] = 1
		else :
			sum = 0
			for j in range(i) :
				sum += (lower[k][j] * upper[j][i])
			lower[k][i] = int((mat[k][i] - sum) / upper[i][i])

print("Input Matrix :\n")
i = 0
j = 0
for i in range(n) :
	for j in range(n) :
		print(mat[i][j], end = "\t") 
	print() 

print("Lower Triangular Matrix :\n")
i = 0
j = 0
for i in range(n) :
	for j in range(n) :
		print(lower[i][j], end = "\t") 
	print() 

print("Upper Triangular Matrix :\n")
i = 0
j = 0
for i in range(n) :
	for j in range(n) :
		print(upper[i][j], end = "\t") 
	print() 
