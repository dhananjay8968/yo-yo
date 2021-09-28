def l(x) :
	arr = []
	ans = 0
	if len(x) == 1 :
		return 0

	for i in range(len(x)) :
		if x[i] == "1" :
			arr.append(i+1)

	for i in range(len(arr)) :
		if i == 0 :
			if arr[i] > 1 :
				ans += ((arr[i]-1)*(arr[i]-1 + 1))//2
			if len(arr) > 1 :
				mid = (arr[i] + arr[i+1])//2
				ans += ((mid - arr[i])*(1 + mid-arr[i]))//2
				ans += ((arr[i+1]-mid-1)*(arr[i+1]-mid-1 + 1))//2

		if i == (len(arr)-1) :
			if arr[i] < (len(x)) :
				ans += ((len(x)-arr[i])*(1 + len(x)-arr[i]))//2
		elif i > 0 and len(arr) > 1 :
			mid = (arr[i] + arr[i+1])//2
			ans += ((mid - arr[i])*(1 + mid-arr[i]))//2
			ans += ((arr[i+1]-mid-1)*(arr[i+1]-mid-1 + 1))//2

	return ans





t = int(input())

for i in range(t) :
	n = int(input())
	x = input()
	print("Case #", end = "")
	print((i+1),end = "")
	print(":",l(x))
