def powof2(n):
	for i in range(0,n+1):
		if pow(2,i)==n:
			return n
	else:
		return 0
x=int(input())
l=[]
if powof2(x)==x:
	print("0")
else:
	for i in range(1,x):
		l.append(powof2(i))
	v=max(l)
	print(abs(v-x))
