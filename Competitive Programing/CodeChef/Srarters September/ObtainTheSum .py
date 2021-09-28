t = int(input())

for i in range(t) :
	N,S = list(map(int, input().split()))
	ans = (N**2 + N - 2*S)/2 
	
	if int(ans) != ans or ans<=0 or ans > N :
		print(-1)
	else :
		print(int(ans))

