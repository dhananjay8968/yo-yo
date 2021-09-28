t = int(input())

for i in range(t) :
	N,K = list(map(int, input().split()))

	A = list(map(int, input().split()))
	positive = 0
	li_x = [ii for ii in range(N)]

	ans = 0
	for j in range(len(A)) :
		if A[j] > 0 :
			ans += A[j]
			positive += 1

	time = 0
	while time < K and positive < N :
		li = A.copy()
		li_z = li_x.copy()
		for j in li_x:
			if j == 0 and A[j] > 0 :
				if A[-1] == 0 :
					positive +=1
				li[-1] += 1
				if A[1] == 0 :
					positive += 1
				li[1] += 1
				ans += 2
				li_z.remove(j)
				
			elif j!= N-1 and A[j] > 0 :
				if A[j-1] == 0 :
					positive += 1
				li[j-1] += 1
				if A[j+1] == 0 :
					positive += 1
				li[j+1] += 1
				ans += 2
				li_z.remove(j)
			elif j == N-1 and A[j] > 0 :
				if A[0] == 0 :
					positive += 1
				li[0] += 1
				if A[j-1] == 0 :
					positive += 1
				li[j-1] += 1
				ans += 2
				li_z.remove(j)
		A = li.copy()
		li_x = li_z.copy()
		time += 1

	if time != K :
		ans += (K-time)*(N*2)

	print(ans)





