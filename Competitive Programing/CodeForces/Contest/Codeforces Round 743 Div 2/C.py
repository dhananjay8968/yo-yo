def readings(number_of_chapters_to_understand,chapters) :
	if 0 not in number_of_chapters_to_understand :
		return -1

	 


T = int(input())

for i in range(T) :
	n = int(input())
	number_of_chapters_to_understand = []
	chapters = []
	for j in range(n) :
		a = list(map(int, input().split()))
		number_of_chapters_to_understand.append(a[0])
		a.pop(0)
		chapters.append(a)

