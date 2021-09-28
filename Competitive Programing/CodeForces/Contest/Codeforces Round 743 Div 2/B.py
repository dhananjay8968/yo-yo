def swaps(A,B) :
	ans = 0
	s = []
	if A[0] < B[0] :
		return 0
	for i in range(len(B)) :
		if A[i] < B[0] :
			s.append(i)

	ans = min(s) 
	return ans

T = int(input())

for  i in range(T) :
	n = int(input())
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	print(swaps(A,B))