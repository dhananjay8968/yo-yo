def b(arr,n) :
	l = 0
	h = len(arr)-1
	mid = (l+h)//2 
	while l <= h :
		if mid = n :
			return mid


N,Q = list(map(int, input()))
arr = list(map(int, input().split()))

arr1 = set(arr)
arr = list(arr1)

arr.sort()
a = min(arr)
b = max(arr)

for i in range(Q) :
	n = int(input())
	if n < a :
		print(n) 
	elif n > b :
		print(len(arr)+n)

	else :


