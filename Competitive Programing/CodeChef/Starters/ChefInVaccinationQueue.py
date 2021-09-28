t = int(input())

for i in range(t) :
	N,P,X,Y =  list(map(int, input().split()))

	A = list(map(int , input().split()))
	ans = 0

	for j in range(P) :
		if A[j] == 0 :
			ans += X
		else :
			ans += Y

	print(ans)

