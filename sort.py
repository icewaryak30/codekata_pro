k=int(input())
l=[]
for i in range(k):
	x=[int(i) for i in input().split()]
	for i in x:
		l.append(i)
p=sorted(l)
print(*p)
