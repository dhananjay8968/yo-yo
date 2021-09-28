t = int(input())

for i in range(t) :
	N,X = list(map(int, input().split()))

	arr = list(map(int, input().split()))
	arr2 = arr.copy()

	while len(arr) > 0 :
		arr2.pop(0)
		if (X-arr[0]) in arr2 :
			arr2.remove(X-arr[0])
			arr = arr2.copy()
		else :
			print(-1)
			break
	if len(arr) == 0 :
		print("Successfully done")