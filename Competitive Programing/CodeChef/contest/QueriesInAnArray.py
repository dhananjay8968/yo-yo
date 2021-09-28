import bisect

n,Q = list(map(int , input().split()))
A = list(map(int, input().split()))

for i in range(Q) :
	l,r,x = list(map(int, input().split()))
	ans = bisect.bisect_left(A,x)
	if ans+1 >= l and ans+1 <= r :
		print(r-ans)
	elif ans+1 < l :
		print(r-l+1)
	else :
		print(0)

