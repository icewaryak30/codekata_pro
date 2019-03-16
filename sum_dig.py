def dig(num):
	s=str(num)
	c=0
	for i in s:
		c+=int(i)
	return c
n=int(input())
k=0
x=[]
for i in range(n):
	if i+dig(i)==n:
		k+=1
		x.append(i)
print(k)
for i in x:
	print(i)
