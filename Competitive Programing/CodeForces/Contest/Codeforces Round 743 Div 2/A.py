def sum(arr) :
	ans = 0 
	for i in range(len(arr)) :
		ans += int(arr[i])
		if int(arr[i]) != 0 and i != (len(arr)-1) :
			ans += 1 

	return ans

t = int(input())

for i in range(t) :
	n = int(input())

	clock = input()

	print(sum(clock))
cdvfrvdfdfgtvevffdddddd
