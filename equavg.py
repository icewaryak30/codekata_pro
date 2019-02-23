def avg(l):
	s=sum(l)
	a=s//len(l)
	return a
n=int(input())
l=[int(i) for i in input().split()]
x=[]
for i in range(len(l)-1):
	x.append(l[0])
	l.remove(l[0])
	if avg(l)==avg(x):
		result="yes"
		break
	else:
		result="no"
print(result)
