n=int(input())
l=[int(i) for i in input().split()]
y=[]
x=[[l[i],l[j],l[k]]  for i in range(len(l)) for j in range(len(l)) for k in range(len(l)) if l[i]<l[j]<l[k] and i<j<k and i!=j!=k]
for i in x:
	if i not in y:
		y.append(i)
print(len(y))
