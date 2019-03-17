n,a,b=map(int,input().split())
if n%2==0:
	x=n//2
	for i in range(n):
		if (i*a)+(i*b)==x:
			p="YES"
			break
		elif i*a==x or i*b==x:
			p="YES"
			break
		else:
			p="NO"
else:
	p="NO"
print(p)
