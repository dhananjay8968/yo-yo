t = int(input())

for i in range(t) :
	S = input()
	ans = 0

	a = S[0]
	if a == "0" :
		ans += 1

	for j in range(len(S)) :
		if S[j] != a :
			a = S[j]
			ans += 1

	print(ans)