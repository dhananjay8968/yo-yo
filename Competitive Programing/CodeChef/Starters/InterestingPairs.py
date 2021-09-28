t = int(input())

for i in range(t) :
	n = int(input())
	ans = 0
	A = list(map(int, input().split()))

	for j in range(len(A)-1) :
		for ii in range(j+1 , len(A)) :
			if (A[j]*A[ii])%((ii+1)*(j+1)) == 0 :
				ans += 1

	print(ans)