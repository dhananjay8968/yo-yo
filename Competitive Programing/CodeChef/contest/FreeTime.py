def best_time(end ,time):
	ans = 0
	while len(end_1) > 0 and len(end_2) > 0 :
		a = min(end)
		ans.append(a)
		i = 0
		while True :
			if time[i][0] <= a :
				time.pop(i)
				end.pop(i)
			else :
				i += 1
			if i == len(time) :
				break
	print(len(ans))
	return ans

N,M = list(map(int, input().split()))

time_1 = []
end_1 = []
time_2 = []
end_2 = []

for i in range(N) :
	x = list(map(int, input().split()))
	time_2.append(x)
	end_1.append(x[1])
for i in range(M) :
	x = list(map(int, input().split()))
	time_2.append(x)
	end_2.append(x[1])

ans = best_time(end, time)

for i in ans :
	print(i, end  = " ")