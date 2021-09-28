t = int(input())

for i in range(t) :
	N = int(input())

	if N%2 == 0 :
		for j in range(N) :
			for ii in range(N) :
				print(-1 , end = " ")

			print()
	else :
		for j in range(N) :
			for ii in range(N) :
				if j == ii :
					print(-1 , end = " ")
				else :
					print(1 , end = " ")

			print()
