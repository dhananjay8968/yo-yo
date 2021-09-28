t = int(input()) 
for i in range(t) :
	TS = int(input())

	if TS%2 != 0 :
		print(TS//2)

	else :
		while TS%2 == 0 :
			TS = TS//2

		print(TS//2)