s=input()
l=[]
c=0
x=s.replace(" ","")
x=x.lower()
for i in range(97,123):
	l.append(chr(i))
for i in l:
	if i in x:
		c+=1
	elif i not in x:
		p="no"
		break
if c>=26:
	p="yes"
else:
	p="no"
print(p)
