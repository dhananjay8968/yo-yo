t = int(input())

for i in range(t) :
	P,a,b,c,x,y = list(map(int, input().split()))

	bujdet_anar = b + x*a 
	bujdet_chakri = c + a*y 

	if bujdet_chakri<= bujdet_anar :
		l = bujdet_chakri
		h = bujdet_anar
	else :
		l = bujdet_anar
		h = bujdet_chakri

	ans = 0

	ans += P//l 
	z = P%l 
	ans += z//h

	print(ans)